from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def check_out(self):
        self.driver.find_element(By.ID, "checkout").click()

    def remove_product(self, product_name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for item in items:
            if product_name in item.text:
                item.find_element(By.CLASS_NAME, "cart_button").click()  # Adjust if needed for remove button
                break
