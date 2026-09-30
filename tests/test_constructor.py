from selenium.webdriver.common.by import By

from locators import Constructor


def test_constructor_buns(authorized_user):
    driver = authorized_user

    tab = driver.find_element(*Constructor.BUNS_TAB)
    driver.execute_script("arguments[0].click();", tab)
    
    assert driver.find_element(By.XPATH, "//h2[text()='Булки']").is_displayed()


def test_constructor_sauces(authorized_user):
    driver = authorized_user

    driver.find_element(*Constructor.SAUCES_TAB).click()

    assert driver.find_element(By.XPATH, "//h2[text()='Соусы']").is_displayed()


def test_constructor_fillings(authorized_user):
    driver = authorized_user

    driver.find_element(*Constructor.FILLINGS_TAB).click()

    assert driver.find_element(By.XPATH, "//h2[text()='Начинки']").is_displayed()