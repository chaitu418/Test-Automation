from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_product_to_cart(self, product_id: str):
        """Add a product to the cart by its ID."""

        add_to_cart_button = self.driver.find_element(By.ID, product_id)
        add_to_cart_button.click()

    def go_to_cart(self):
        """Navigate to the cart page."""
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

    def proceed_to_checkout(self):
        """Proceed to the checkout page."""
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """Fill out the checkout information form."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def complete_checkout(self):
        """Complete the checkout process."""
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

    def get_checkout_confirmation_message(self):
        """Get the confirmation message after completing checkout."""
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text

    def get_error_message(self):
        """Get the error message displayed on the checkout page."""
        return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text

    def is_continue_button_enabled(self):
        """Check if the 'Continue' button is enabled."""
        continue_button = self.driver.find_element(By.ID, "continue")
        return continue_button.is_enabled()
