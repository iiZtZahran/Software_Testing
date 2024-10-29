from selenium.webdriver.common.by import By

def test_checkout_without_details(login_page, inventory_page, cart_page, checkout_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    cart_page.check_out()

    # Click continue without entering details
    checkout_page.driver.find_element(By.ID, "continue").click()
    error_message = checkout_page.driver.find_element(By.CLASS_NAME, "error-message-container").text

    assert "Error: First Name is required" in error_message
