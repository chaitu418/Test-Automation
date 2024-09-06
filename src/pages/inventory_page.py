from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    inventory_list_locator = (By.CLASS_NAME, "inventory_list")
    product_item_locator = (By.CLASS_NAME, "inventory_item")
    product_sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    cart_badge_locator = (By.CLASS_NAME, "shopping_cart_badge")
    add_to_cart_button_locator = (By.XPATH, "//button[text()='Add to cart']")
    remove_button_locator = (By.XPATH, "//button[text()='Remove']")

    # Wait for inventory page to load
    def wait_for_page_to_load(self):
        self.wait.until(EC.presence_of_element_located(self.inventory_list_locator))

    # Get the page title
    def get_page_title(self):
        return self.driver.title

    # Get the list of product elements
    def get_all_products(self):
        return self.driver.find_elements(*self.product_item_locator)

    # Add a product to the cart
    def add_first_product_to_cart(self):
        add_button = self.driver.find_element(*self.add_to_cart_button_locator)
        add_button.click()

    # Remove a product from the cart
    def remove_first_product_from_cart(self):
        remove_button = self.driver.find_element(*self.remove_button_locator)
        remove_button.click()

    # Get the cart badge value (i.e., number of items in cart)
    def get_cart_badge_count(self):
        return self.driver.find_element(*self.cart_badge_locator).text

    # Sort products by given option (text of the sort option)
    def sort_products(self, option_text):
        sort_dropdown = self.driver.find_element(*self.product_sort_dropdown)
        sort_dropdown.click()
        sort_option = self.driver.find_element(By.XPATH, f"//option[text()='{option_text}']")
        sort_option.click()

    # Get product prices (to verify sorting)
    def get_product_prices(self):
        prices_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text.replace("$", "")) for price in prices_elements]
        return prices

    def go_back(self):
        self.driver.back()