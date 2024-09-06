import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()