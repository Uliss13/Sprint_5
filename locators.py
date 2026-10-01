from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")                             # Кнопка «Войти в аккаунт»
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")                               # Кнопка «Личный кабинет»
    CONSTRUCTOR = (By.XPATH, ".//a[.//*[contains(text(), 'Конструктор')]]")                                       # Кнопка «Конструктор»
    LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]//*[local-name()='svg']")          # Логотип Stellar Burgers


class LoginPage:
    EMAIL_INPUT = (By.XPATH, ".//div[contains(@class, 'input_type_text')]//input[@name='name']")            # Поле Email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль' and @type='password']")                            # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")                                       # Кнопка «Войти»
    REGISTER_LINK = (By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]")                              # Ссылка «Зарегистрироваться»
    RECOVER_LINK = (By.XPATH, ".//a[contains(text(), 'Восстановить пароль')]")                              # Ссылка «Восстановить пароль»


class RegistrationPage:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")                              # Поле Имя
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")                           # Поле Email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль' and @type='password']")                            # Поле Пароль
    REGISTER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")                       # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, ".//a[contains(text(), 'Войти')]")                                              # Ссылка «Войти»


class RecoverPage:
    LOGIN_LINK = (By.XPATH, ".//a[contains(text(), 'Войти')]")                                              # Ссылка «Войти»


class Constructor:
    BUNS_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][.//span[text()='Булки']]")                   #  «Булки»
    SAUCES_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][.//span[text()='Соусы']]")                 #  «Соусы»
    FILLINGS_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab')][.//span[text()='Начинки']]")             # «Начинки»

    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")

class ProfilePage:
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")                                      # Кнопка «Выход»