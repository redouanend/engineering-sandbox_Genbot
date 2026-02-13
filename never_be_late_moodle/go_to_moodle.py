from playwright.sync_api import sync_playwright, Page
from playwright_debug import print_dom
from playwright_helper import isElementExisting
from login import login
from api_moodle import get_assignments_due_from_moodle_dashboard
from create_deposit_folders import create_deposit_folders


def main():
    with sync_playwright() as p:
        #Open a persistent context to have persistent connexion to moodle
        context = p.chromium.launch_persistent_context(
            user_data_dir="./browser_profile", 
            headless=False
        )
        page = context.pages[0] 

        page.goto("https://moodle.epf.fr/")
        # Avoid hard failing on a fixed timeout: first login + 2FA can take longer.
        # We will decide whether to login using a safe existence check below.
        page.wait_for_load_state("domcontentloaded")
        
        if isElementExisting(page, "text=Connexion"):
            login(page) 
        else:
            print("Vous êtes déja connectés !")

        page.goto("https://moodle.epf.fr/my/")
        page.wait_for_load_state("domcontentloaded")

        assignments = get_assignments_due_from_moodle_dashboard(page)
        create_deposit_folders(assignments)
        
        # Return extracted assignments so the GUI can display them.
        return assignments

if __name__ == "__main__":
    main()
