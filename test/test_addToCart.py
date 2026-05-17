from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_add_to_cart(driver_logged):
     driver_logged.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
     driver_logged.find_element(By.CLASS_NAME, "shopping_cart_link").click()
     assert "/cart.html" in driver_logged.current_url
     
     items = driver_logged.find_elements(By.CLASS_NAME, "cart_item")
     assert len(items) > 0
          