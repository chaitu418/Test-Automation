import os
import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import datetime
from resources.config.conftest import setup

user_data = [
    {"username":"standard_user","password": "secret_sauce"},
    {"username": "locked_out_user","password": "secret_sauce"},
    {"username": "problem_user","password": "secret_sauce"},
    {"username": "performance_glitch_user","password": "secret_sauce"},
    {"username": "error_user","password": "secret_sauce"},
    {"username": "error_user","password": "secret_sauce"},
    {"username": "visual_user","password": "secret_sauce"}]


@pytest.mark.parametrize("user", user_data)

#6. Test to check login with valid credentials
def test_valid_login(setup,user):
    driver=setup
    login_page = LoginPage(setup)
    login_page.enter_username(user["username"])
    login_page.enter_password(user["password"])
    login_page.click_login()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

#7. Test to check login with invalid credentials
def test_invalid_login(setup):
    driver=setup
    login_page = LoginPage(setup)
    login_page.enter_username("invalid_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Failed. Username and password do not match any user in this service" in error_message
    logger.error(f"Login failed for user {user['username']}")


