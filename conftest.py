import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers import BASE_URL, NAME, PASSWORD, email_generator
from locators import LoginPage, RegistrationPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    email = email_generator()

    driver.get(f"{BASE_URL}/register")

    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(NAME)
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_contains("/login")
    )

    yield email, PASSWORD


@pytest.fixture
def authorized_user(driver, registered_user):
    email, password = registered_user

    driver.get(f"{BASE_URL}/login")

    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.url_changes(f"{BASE_URL}/login")
    )

    yield driver
