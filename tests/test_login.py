import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_login_page_title(driver):
    assert driver.title == "Swag Labs"


def test_login_success(driver):
    login(driver, "standard_user", "secret_sauce")

    titre = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titre.text == "Products"
    assert "inventory" in driver.current_url


@pytest.mark.parametrize(
    "username, password, message_attendu",
    [
        ("standard_user", "mauvais_mdp",
         "Username and password do not match any user in this service"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "this user has been locked out"),
    ],
)
def test_login_errors(driver, username, password, message_attendu):
    login(driver, username, password)

    erreur = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert message_attendu in erreur.text