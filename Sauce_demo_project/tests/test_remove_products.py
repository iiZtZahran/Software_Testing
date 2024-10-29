from selenium.webdriver.common.by import By

def test_remove_product_from_cart(login_page, inventory_page, cart_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    # Remove the product from the cart
    cart_page.driver.find_element(By.CLASS_NAME, "cart_item").find_element(By.CLASS_NAME, "btn_secondary").click()

    # Assert that the cart is empty
    assert "Your cart is empty" in cart_page.driver.page_source