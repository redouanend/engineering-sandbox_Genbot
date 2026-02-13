from playwright.sync_api import sync_playwright, Page

def isElementExisting(page: Page, selector: str) -> bool:
    """
    Checks if an element exists on the page.
    :param page: The page (playwright object) to check the element of.
    :param selector: The selector to check the element of.
    :return: True if the element exists, False otherwise.
    """
    return page.locator(selector).count() > 0