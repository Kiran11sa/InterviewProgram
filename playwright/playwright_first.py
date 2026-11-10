from playwright.sync_api import sync_playwright
import time
def test_launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        print("Title is:", page.title())
        time.sleep(10)
        browser.close()