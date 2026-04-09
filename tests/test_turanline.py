from playwright.sync_api import sync_playwright

BASE_URL = "https://www.turanline.com"

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(BASE_URL)
        assert "TuranLine" in page.title()
        browser.close()

def test_login_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("networkidle")
        assert page.url != BASE_URL
        browser.close()

def test_login_blank_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("networkidle")
        page.locator(".signBtn").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_blank_login.png")
        browser.close()

def test_login_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("networkidle")
        page.get_by_role("textbox").nth(1).fill("9001234567")
        page.locator('input[type="password"]').fill("wrongpassword")
        page.locator(".signBtn").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_invalid_login.png")
        browser.close()