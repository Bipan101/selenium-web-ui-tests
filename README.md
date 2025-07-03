# Selenium Automated Website Testing for test.com

This repository contains a **comprehensive automated testing suite** built with **Python and Selenium WebDriver** to test the functionality and UI of a sample website hosted at `https://test.com`.

---

## 🔍 Features Tested

### 🏠 Homepage
- Page load verification
- Navigation link checks
- Hero section validation
- Call-to-action (CTA) button detection
- Image presence and broken image detection

### 🔐 Login Page
- Field presence: username, password, login button
- Validation messages for empty inputs
- Handling of invalid login attempts
- Functionality of the “Forgot Password” link

### 🧾 Registration Page
- Detection of required fields:
  - Mobile Number, Email, First Name, Last Name, Password, Confirm Password
- Validations:
  - Empty form submission
  - Invalid email format
  - Password mismatch
  - Short/invalid mobile number
  - Long input edge cases
- Successful registration flow (or duplicate handling)
- Terms checkbox, privacy policy link, and login link

### 🔁 Forgot Password Page
- Presence of input field and submit button
- Proper validation on empty input

### 🌐 Cross-Browser Compatibility
- JavaScript check (e.g., jQuery presence)
- CSS style loading
- Viewport responsiveness (mobile support)

---

## 🛠 Technologies Used

- Python 3.x
- Selenium WebDriver
- ChromeDriver (via `webdriver-manager`)
- WebDriverWait with expected conditions
- JSON report generation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/testcom-selenium-tests.git
cd testcom-selenium-tests
```

### 2. Install Dependencies

```bash
pip install selenium webdriver-manager
```

### 3.Run the Tests
```bash
python test_script.py
```
After running, a test report is saved to:
test.json file
