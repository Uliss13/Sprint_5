from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPage, ProfilePage


class TestProfile:

    def test_go_to_profile(self, authorized_user):
        driver = authorized_user
        driver.find_element(*MainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/account/profile")
        )
        assert "/account/profile" in driver.current_url

    def test_logout(self, authorized_user):
        driver = authorized_user
        driver.find_element(*MainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/account/profile")
        )
        driver.find_element(*ProfilePage.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains("/login")
        )
        assert "/login" in driver.current_url