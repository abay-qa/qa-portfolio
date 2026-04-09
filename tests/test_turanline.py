from playwright.sync_api import sync_playwright

BASE_URL = "https://www.turanline.com"

def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(BASE_URL)
        page.wait_for_load_state("domcontentloaded")
        assert "TuranLine" in page.title()
        browser.close()

def test_login_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        assert page.url != BASE_URL
        browser.close()

def test_login_blank_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        page.locator(".signBtn").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_blank_login.png")
        browser.close()

def test_login_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("textbox").nth(1).fill("9001234567")
        page.locator('input[type="password"]').fill("wrongpassword")
        page.locator(".signBtn").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_invalid_login.png")
        browser.close()

def test_homepage_has_categories():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(BASE_URL)
        page.wait_for_load_state("domcontentloaded")
        assert page.locator('a[href="/women"]').count() > 0
        assert page.locator('a[href="/men"]').count() > 0
        assert page.locator('a[href="/kids"]').count() > 0
        browser.close()

def test_language_switch_to_russian():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/ru")
        page.wait_for_load_state("domcontentloaded")
        assert "/ru" in page.url
        browser.close()

def test_catalog_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/catalog")
        page.wait_for_load_state("domcontentloaded")
        assert "catalog" in page.url
        browser.close()

def test_contact_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/contacts")
        page.wait_for_load_state("domcontentloaded")
        assert "contact" in page.url.lower()
        browser.close()

def test_security_sql_injection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("textbox").nth(1).fill("' OR 1=1 --")
        page.locator('input[type="password"]').fill("' OR 1=1 --")
        page.locator(".signBtn").click()
        page.wait_for_timeout(3000)
        page.screenshot(path="turanline_sql_injection.png")
        assert page.url != f"{BASE_URL}/dashboard"
        assert page.url != f"{BASE_URL}/profile"
        browser.close()

def test_security_xss():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("textbox").nth(1).fill("<script>alert('xss')</script>")
        page.locator('input[type="password"]').fill("<script>alert('xss')</script>")
        page.locator(".signBtn").click()
        page.wait_for_timeout(3000)
        page.screenshot(path="turanline_xss.png")
        assert page.url != f"{BASE_URL}/dashboard"
        assert page.url != f"{BASE_URL}/profile"
        browser.close()

def test_security_long_input():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{BASE_URL}/login")
        page.wait_for_load_state("domcontentloaded")
        long_string = "A" * 1000
        page.get_by_role("textbox").nth(1).fill(long_string)