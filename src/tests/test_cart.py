import pytest
from selenium import webdriver
from src.pages.cart_page import CartPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def login(driver, username="standard_user", password="secret_sauce"):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# Test case 8: Test to check whehter customer is successfully checking out and placing order
def test_successful_checkout(driver):
    login(driver)
    cart = CartPage(driver)
    cart.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    cart.add_product_to_cart("add-to-cart-sauce-labs-bike-light")
    cart.go_to_cart()
    cart.proceed_to_checkout()
    cart.fill_checkout_information("John", "Doe", "12345")
    cart.complete_checkout()

    success_message = cart.get_checkout_confirmation_message()
    assert success_message == 'Thank you for your order!'


# Test case 9: Test to check whether error name is displayed without entering delivery details
def test_checkout_missing_info(driver):
    login(driver)
    cart = CartPage(driver)
    cart.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    cart.go_to_cart()
    cart.proceed_to_checkout()
    cart.driver.find_element(By.ID, "continue").click()

    error_message = cart.get_error_message()
    assert error_message == "Error: First Name is required", f"Expected 'Error: First Name is required' but got" \
                                                             f" '{error_message}'"


# Test case 10: Test to check the disability of continue button without entering credentials
def test_checkout_button_disabled(driver):
    login(driver)
    cart = CartPage(driver)
    cart.go_to_cart()
    cart.proceed_to_checkout()

    assert not cart.is_continue_button_enabled(), "Continue button should be disabled initially"
