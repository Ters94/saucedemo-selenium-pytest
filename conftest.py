import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
   
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    yield driver      

    driver.quit()    


@pytest.fixture
def logged_in_driver(driver):
    """Driver déjà connecté avec un utilisateur valide."""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    return driver