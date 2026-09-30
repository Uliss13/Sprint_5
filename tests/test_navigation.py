from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers import BASE_URL
from locators import MainPage


def test_go_to_constructor(authorized_user):
    driver = authorized_user

    driver.find_element(*MainPage.CONSTRUCTOR).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(f"{BASE_URL}/")
    )

    assert driver.current_url == f"{BASE_URL}/"


def test_go_to_constructor_by_logo(authorized_user):
    driver = authorized_user

    driver.find_element(*MainPage.LOGO).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_to_be(f"{BASE_URL}/")
    )

    assert driver.current_url == f"{BASE_URL}/"
