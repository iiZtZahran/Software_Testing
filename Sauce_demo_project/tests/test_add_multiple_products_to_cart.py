from selenium.webdriver.common.by import By


def test_add_multiple_products_to_cart(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.go_to_cart()

    cart_items = inventory_page.driver.find_elements(By.CLASS_NAME, "cart_item")
    product_names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in cart_items]

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names

