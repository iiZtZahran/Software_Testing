from selenium.webdriver.common.by import By

def test_add_product_to_cart(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    cart_items = inventory_page.driver.find_elements(By.CLASS_NAME, "cart_item")
    assert any("Sauce Labs Backpack" in item.text for item in cart_items)
    assert "cart" in inventory_page.driver.current_url
