from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import USERNAME, VALID_EMAIL, INVALID_PASSWORD, REGISTER_URL
from locators import RegistrationPageLocators, LoginPageLocators
from helpers import generate_unique_email


class TestRegistration:
    def test_registration_valid_password(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Алексей")
        random_email = generate_unique_email()
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Parol1")
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
        assert 'Войти' in login_button.text

    def test_registration_invalid_password(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(USERNAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        assert error_message.text == "Некорректный пароль"
