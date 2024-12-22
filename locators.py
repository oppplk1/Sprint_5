from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа в аккаунт
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  # Кнопка выбора секции Булок
    BUN_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")  # Флюоресцентная булка R2-D3
    SAUCES_SECTION = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Соусы']")
    # Кнопка выбора секции Соусов
    SAUCE_1 = (By.XPATH, "//p[text()='Соус Spicy-X']")  # Соус Spicy-X
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Кнопка выбора секции Начинок
    FILLING_1 = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")
    # Мясо бессмертных моллюсков Protostomia
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка для перехода в Личный Кабинет
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка для перехода на страницу Конструктора
    LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип в шапке сайта


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")  # Окно ввода Имени
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Окно ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Окно ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка Зрегистрироваться
    LOGIN_REDIRECT = (By.XPATH, "//a[@href='/login']")  # Кнопка на страницу Входа
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Сообщение об ошибке


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Окно ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Окно ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка Войти
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Переход на окно Зарегистрироваться
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Переход на окно Восстановить пароль


class PersonalAccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выйти
