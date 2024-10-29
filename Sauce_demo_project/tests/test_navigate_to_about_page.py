from selenium.webdriver.common.by import By


def test_navigate_to_about_page(login_page):
    login_page.login("standard_user", "secret_sauce")
    login_page.driver.find_element(By.XPATH, "//a[contains(text(), 'About')]").click()

    assert "Sauce Labs" in login_page.driver.title
