import pytest

from helpers import BASE_URL, NAME, email_generator
from locators import RegistrationPage


def test_register_success(driver, registered_user):
    assert "/login" in driver.current_url


def test_register_short_password(driver):
    email = email_generator()
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(NAME)
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys("123")
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    assert "/register" in driver.current_url