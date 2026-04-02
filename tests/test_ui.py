from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://google.com")
        assert "Google" in page.title()
        browser.close()

def test_click_category():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://books.toscrape.com")
        page.get_by_text("Mystery").click()
        page.wait_for_load_state("networkidle")
        assert "mystery" in page.url
        browser.close()

def test_bookstore_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://books.toscrape.com")
        assert "Books" in page.title()
        browser.close()

def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://books.toscrape.com")
        page.screenshot(path="bookstore.png")
        assert page.title() != ""
        browser.close()

def test_wrong_page_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://books.toscrape.com")
        try:
            assert "Amazon" in page.title()
        except AssertionError:
            page.screenshot(path="failure_screenshot.png")
            raise
        browser.close()