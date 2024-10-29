from selenium.webdriver.common.by import By
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            if product_name in product.text:
                product.find_element(By.CLASS_NAME, "btn_inventory").click()
                break

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
