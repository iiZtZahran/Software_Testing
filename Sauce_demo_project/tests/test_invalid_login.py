from selenium.webdriver.common.by import By
def test_invalid_login(login_page):
    login_page.login("invalid_user", "invalid_pass")
    error_message = login_page.driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error_message