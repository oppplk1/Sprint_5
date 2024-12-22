from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import USERNAME, VALID_EMAIL, INVALID_PASSWORD, REGISTER_URL
from locators import RegistrationPageLocators


class TestRegistration:
    def test_registration_valid_password(self):
        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Алексей")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("alexeyorlov15941@yandex.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Parol1")
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        login_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
        assert 'Войти' in login_button.text, "Тест пройден"
        driver.quit()

    def test_registration_invalid_password(self):
        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(USERNAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))
        assert error_message.text == "Некорректный пароль"
        print("Тест пройден: некорректный пароль")
        driver.quit()
