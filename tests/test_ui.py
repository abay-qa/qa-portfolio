from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://google.com")
        assert "Google" in page.title()
        browser.close()

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://duckduckgo.com")
        page.locator('input[name="q"]').fill("QA Engineer")
        page.keyboard.press("Enter")
        page.wait_for_load_state("networkidle")
        assert "QA Engineer" in page.title()
        browser.close()