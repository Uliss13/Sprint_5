from locators import Constructor


class TestConstructor:

    def test_constructor_buns(self, authorized_user):
        driver = authorized_user
        tab = driver.find_element(*Constructor.BUNS_TAB)
        driver.execute_script("arguments[0].click();", tab)
        assert driver.find_element(*Constructor.BUNS_HEADER).is_displayed()

    def test_constructor_sauces(self, authorized_user):
        driver = authorized_user
        driver.find_element(*Constructor.SAUCES_TAB).click()
        assert driver.find_element(*Constructor.SAUCES_HEADER).is_displayed()

    def test_constructor_fillings(self, authorized_user):
        driver = authorized_user
        driver.find_element(*Constructor.FILLINGS_TAB).click()
        assert driver.find_element(*Constructor.FILLINGS_HEADER).is_displayed()