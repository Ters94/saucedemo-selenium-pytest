import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_page_title(driver):
    assert driver.title == "Swag Labs"


def test_login_success(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"
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
    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert message_attendu in login_page.get_error_message()