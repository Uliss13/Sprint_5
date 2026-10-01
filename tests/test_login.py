from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers import BASE_URL
from locators import MainPage, LoginPage, RegistrationPage, RecoverPage


class TestLogin:

    def test_login_from_main(self, driver, registered_user):
        email, password = registered_user
        driver.get(BASE_URL)
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_changes(f"{BASE_URL}/login")
        )
        assert "/login" not in driver.current_url

    def test_login_from_profile(self, driver, registered_user):
        email, password = registered_user
        driver.get(BASE_URL)
        driver.find_element(*MainPage.PERSONAL_ACCOUNT).click()
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_changes(f"{BASE_URL}/login")
        )
        assert "/login" not in driver.current_url

    def test_login_from_register(self, driver, registered_user):
        email, password = registered_user
        driver.get(f"{BASE_URL}/register")
        driver.find_element(*RegistrationPage.LOGIN_LINK).click()
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_changes(f"{BASE_URL}/login")
        )
        assert "/login" not in driver.current_url

    def test_login_from_recover(self, driver, registered_user):
        email, password = registered_user
        driver.get(f"{BASE_URL}/forgot-password")
        driver.find_element(*RecoverPage.LOGIN_LINK).click()
        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_changes(f"{BASE_URL}/login")
        )
        assert "/login" not in driver.current_url