# import pytest for testing
import pytest
# import selenium webdriver module
from selenium import webdriver
# imports the By class, which helps to locate elements on a web page
from selenium.webdriver.common.by import By
#import python built in time module
import time


# Fixture to launch and quit the browser
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Test Case: Positive Login and Validate title + dashboard URL
def test_positive_login(driver):
    driver.get("https://www.saucedemo.com/")

    # Validate homepage URL
    assert driver.current_url == "https://www.saucedemo.com/"

    # Validate title of the login page
    assert driver.title == "Swag Labs"

    # Perform login with valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Validate dashboard URL after login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert driver.title == "Swag Labs"


# Test Case: Negative Login (wrong password) and remain on login page
def test_negative_login(driver):
    driver.get("https://www.saucedemo.com/")

    # Attempt login with invalid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Still on login page — URL must not change
    assert driver.current_url == "https://www.saucedemo.com/"

    # Validate error message
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic error" in error
