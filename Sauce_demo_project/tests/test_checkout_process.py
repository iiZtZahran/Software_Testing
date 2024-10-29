from selenium.webdriver.common.by import By

# Additional test to ensure correct checkout process
def test_checkout_process(login_page, inventory_page, cart_page, checkout_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    cart_page.check_out()
    checkout_page.enter_details_and_continue("John", "Doe", "12345")

    # Assert that the checkout step two page is reached
    assert "checkout-step-two" in checkout_page.driver.current_url