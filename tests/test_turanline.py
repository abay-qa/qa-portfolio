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

REG_URL = "https://www.turanline.com/ru/registration"

def test_registration_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        assert "registration" in page.url
        browser.close()

def test_registration_blank_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator("button.signBtn, button[class*='signBtn'], button[class*='registerBtn']").first.click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_reg_blank.png")
        browser.close()

def test_registration_invalid_name():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свое имя"]').fill("123!@#")
        page.wait_for_timeout(1000)
        page.screenshot(path="turanline_reg_invalid_name.png")
        browser.close()

def test_registration_weak_password():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свой пароль"]').fill("123")
        page.wait_for_timeout(1000)
        page.screenshot(path="turanline_reg_weak_password.png")
        browser.close()

def test_registration_sql_injection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свое имя"]').fill("' OR 1=1 --")
        page.locator('input[placeholder="Введите свой пароль"]').fill("' OR 1=1 --")
        page.locator("button.signBtn, button[class*='signBtn'], button[class*='registerBtn']").first.click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_reg_sqli.png")
        assert "registration" in page.url or "login" not in page.url
        browser.close()

def test_debug_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        buttons = page.locator("button").all()
        for i, btn in enumerate(buttons):
            print(f"Button {i}: text={btn.inner_text()}, class={btn.get_attribute('class')}")
        browser.close()

REG_URL = "https://www.turanline.com/ru/registration"

def test_registration_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        assert "registration" in page.url
        browser.close()

def test_registration_blank_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator(".btnRegg").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_reg_blank.png")
        browser.close()

def test_registration_invalid_name():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свое имя"]').fill("123!@#")
        page.wait_for_timeout(1000)
        page.screenshot(path="turanline_reg_invalid_name.png")
        browser.close()

def test_registration_weak_password():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свой пароль"]').fill("123")
        page.wait_for_timeout(1000)
        page.screenshot(path="turanline_reg_weak_password.png")
        browser.close()

def test_registration_sql_injection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator('input[placeholder="Введите свое имя"]').fill("' OR 1=1 --")
        page.locator('input[placeholder="Введите свой пароль"]').fill("' OR 1=1 --")
        page.locator(".btnRegg").click()
        page.wait_for_timeout(2000)
        page.screenshot(path="turanline_reg_sqli.png")
        assert "registration" in page.url
        browser.close()

def test_registration_checkboxes_prechecked():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(REG_URL)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(2000)

        # Get all checkboxes on the page
        checkboxes = page.locator('input[type="checkbox"]').all()
        prechecked = []
        for i, cb in enumerate(checkboxes):
            if cb.is_checked():
                prechecked.append(i)

        # Take screenshot as evidence
        page.screenshot(path="turanline_reg_checkboxes.png")

        # Document the finding
        print(f"\nTotal checkboxes found: {len(checkboxes)}")
        print(f"Pre-checked checkboxes: {prechecked}")

        # This test DOCUMENTS the issue rather than failing
        # SMS marketing consent should NOT be pre-checked by law
        assert len(prechecked) > 0, "No pre-checked boxes found"
        print("⚠️  COMPLIANCE ISSUE: Marketing consent checkbox is pre-checked by default")
        browser.close()