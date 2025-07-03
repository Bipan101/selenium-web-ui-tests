# ... (imports remain unchanged)

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Automatically download and use the correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Global test results storage
test_results = {
    "summary": {},
    "detailed_results": {},
    "errors": [],
    "warnings": []
}

# ... (log_result and safe_find_element remain unchanged)

def test_page_load(url, page_name, expected_title_contains=""):
    """Test basic page loading"""
    try:
        driver.get(url)
        time.sleep(3)

        title = driver.title
        current_url = driver.current_url

        # Check for 404 or error pages
        page_source = driver.page_source.lower()
        is_404 = any(error in page_source for error in ['404', 'not found', 'page not found'])
        is_error = any(error in page_source for error in ['500 error', 'server error', 'error occurred'])

        if is_404:
            log_result(f"{page_name} - Page Load", False, f"Title: {title}", "404 Page Not Found")
            return False
        elif is_error:
            log_result(f"{page_name} - Page Load", False, f"Title: {title}", "Server Error")
            return False
        else:
            details = f"Title: {title} | URL: {current_url}"
            log_result(f"{page_name} - Page Load", True, details)
            return True

    except Exception as e:
        log_result(f"{page_name} - Page Load", False, "", str(e))
        return False

def test_homepage_functionality():
    """Test homepage specific functionality"""
    if not test_page_load("https://test.com/", "Homepage"):
        return
    # ... (rest of function remains unchanged)

def test_login_functionality():
    """Test login page functionality"""
    if not test_page_load("https://test.com/User/Login", "Login Page"):
        return
    # ... (rest of function remains unchanged)

def test_register_functionality():
    """Test registration page comprehensive functionality"""
    if not test_page_load("https://test.com/User/Register", "Register Page"):
        return
    # ... (rest of function remains unchanged)

def test_forgot_password_functionality():
    """Test forgot password page functionality"""
    if not test_page_load("https://test.com/User/ForgotPassword", "Forgot Password Page"):
        return
    # ... (rest of function remains unchanged)

def test_cross_browser_compatibility():
    """Test basic cross-browser compatibility features"""
    try:
        # Test JavaScript functionality
        driver.get("https://test.com/")
        time.sleep(2)
        # ... (rest remains unchanged)
    except Exception as e:
        log_result("Cross-browser - Compatibility", False, "", str(e))

# ... (generate_report and main execution remain unchanged)