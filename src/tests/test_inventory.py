import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.inventory_page import InventoryPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Login
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    yield driver
    driver.quit()


# Test case 1: Verify page title
def test_inventory_page_title(setup):
    driver = setup
    assert driver.title == "Swag Labs"


# Test case 2: Verify products are listed
def test_products_listed(setup):
    driver = setup
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No products found on the inventory page"


# Test case 3: Add product to the cart and verify the cart badge
def test_add_product_to_cart(setup):
    driver = setup
    first_product_add_btn = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    first_product_add_btn.click()

    # Check if the cart icon shows 1 product
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Product was not added to the cart"


# Test case 4: Verify sorting of products (if sorting feature exists)
def test_sort_products_by_price(setup):
    driver = setup
    # Find the sort dropdown and sort by 'Price (low to high)'
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()
    sort_dropdown.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()

    # Check the first product's price is less than the second product's price
    prices = [float(p.text[1:]) for p in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    assert prices == sorted(prices), "Products are not sorted by price correctly"


# Test case 5: Verify item can be removed from cart
def test_remove_product_from_cart(setup):
    driver = setup
    first_product_add_btn = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    first_product_add_btn.click()

    # Now click on "Remove" to remove the product
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()

    # Check if the cart badge disappears
    cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badges) == 0, "Product was not removed from the cart"

