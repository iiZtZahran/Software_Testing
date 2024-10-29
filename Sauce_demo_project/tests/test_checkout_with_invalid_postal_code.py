from selenium.webdriver.common.by import By

def test_checkout_with_invalid_postal_code(login_page, inventory_page, cart_page, checkout_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    cart_page.check_out()

    checkout_page.enter_details_and_continue("John", "Doe", "invalid_zip")
    error_message = checkout_page.driver.find_element(By.CLASS_NAME, "error-message-container").text

    assert "Error: Postal Code is required" in error_message

