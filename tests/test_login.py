from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators
from helpers import login


class TestLogin:
    def test_login_main_url(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        login(driver)
        order_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))
        assert order_button.is_displayed()

    def test_login_profile_button(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))
        assert profile_link.is_displayed()

    def test_login_register_url(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.LOGIN_REDIRECT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))
        assert profile_link.is_displayed()

    def test_login_forgot_password_url(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(*RegistrationPageLocators.LOGIN_REDIRECT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))
        assert profile_link.is_displayed()
