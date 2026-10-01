from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers import BASE_URL, NAME, PASSWORD, email_generator
from locators import RegistrationPage


class TestRegistration:

    def test_register_success(self, driver):
        driver.get(f"{BASE_URL}/register")
        email = email_generator()
        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )
        assert "/login" in driver.current_url

    def test_register_short_password(self, driver):
        driver.get(f"{BASE_URL}/register")
        email = email_generator()
        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
        assert "/register" in driver.current_url