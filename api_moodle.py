from playwright.sync_api import Page
import json
from pathlib import Path


def get_assignments_due_from_moodle_dashboard(page: Page) -> list[dict]:
    """
    Extracts from the Moodle dashboard timeline all tasks of type "Devoir doit être rendu"
    (assignments to submit) and returns a list of dicts with link, title, due date and course.

    :param page: Playwright page on the Moodle dashboard (e.g. /my/).
    :return: List of dicts with keys: url, title, due_date_label, due_timestamp, course.
             due_timestamp is the Unix timestamp of the exact deadline (date + time).
    """

    #Verifying that we are on the Moodle dashboard
    if "moodle.epf.fr/my" not in page.url:
        raise ValueError(
            "get_assignments_due_from_moodle_dashboard must be called on the Moodle dashboard."
            f"Current URL: {page.url}"
        )

    #Looking at the interesant div
    container = page.locator('[data-region="event-list-container"]')
    container.wait_for(state="visible", timeout=10000)

    #Waiting for the elemets to be charged 
    page.locator('[data-region="event-list-loading-placeholder"]').wait_for(state="hidden", timeout=15000)

    #Extract the data from the div
    items = page.evaluate("""
        () => {
            const results = [];
            const eventItems = document.querySelectorAll('[data-region="event-list-item"]');
            for (const item of eventItems) {
                const descSmall = item.querySelector('.event-name-container small.mb-0');
                if (!descSmall || !descSmall.textContent.includes('Devoir doit être rendu')) continue;

                const linkEl = item.querySelector('.event-name a[href*="mod/assign/view"]');
                if (!linkEl) continue;

                const timeEl = item.querySelector('.timeline-name small.text-end');
                const time = timeEl ? timeEl.textContent.trim() : '';

                const listGroup = item.closest('.list-group');
                const dateDiv = listGroup && listGroup.previousElementSibling;
                let dateLabel = '';
                let timestamp = null;
                if (dateDiv && dateDiv.getAttribute('data-region') === 'event-list-content-date') {
                    const h5 = dateDiv.querySelector('h5');
                    dateLabel = h5 ? h5.textContent.trim() : '';
                    const ts = dateDiv.getAttribute('data-timestamp');
                    timestamp = ts ? parseInt(ts, 10) : null;
                }

                const course = descSmall.textContent.includes('·')
                    ? descSmall.textContent.split('·')[1].trim()
                    : '';

                results.push({
                    url: linkEl.href,
                    title: linkEl.textContent.trim(),
                    due_date_label: dateLabel,
                    due_timestamp: timestamp,
                    time: time,
                    course: course
                });
            }
            return results;
        }
    """)

    # due_timestamp from Moodle is midnight of the due day; add time (HH:MM) to get real deadline
    for item in items:
        ts = item.get("due_timestamp")
        time_str = (item.get("time") or "").strip() #Strip in case Moodle does shit
        if ts is not None and time_str and ":" in time_str:
            parts = time_str.split(":")
            try:
                hour = int(parts[0].strip())
                minute = int(parts[1].strip()) if len(parts) > 1 else 0
                item["due_timestamp"] = ts + hour * 3600 + minute * 60
            except (ValueError, IndexError):
                pass
        item.pop("time", None) #we can remove time from the dictionnary since it's in the due_timestamp


    #Before returning items, saving it in a json file so that we can access it later
    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / "assignments.json", "w") as f:
        json.dump(items, f)
    
    return items
