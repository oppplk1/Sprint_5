from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from locators import MainPageLocators, RegistrationPageLocators
from helpers import login


class TestLogin:
    def test_login_main_url(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
        assert profile_link.is_displayed(), "Тест пройден, пользователь вошел в личный кабинет"

        driver.quit()

    def test_login_profile_button(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
        assert profile_link.is_displayed(), "Тест пройден, пользователь вошел в личный кабинет"

        driver.quit()

    def test_login_register_url(self):
        driver = webdriver.Chrome()
        driver.get(REGISTER_URL)

        driver.find_element(*RegistrationPageLocators.LOGIN_REDIRECT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
        assert profile_link.is_displayed(), "Тест пройден, пользователь вошел в личный кабинет"

        driver.quit()

    def test_login_forgot_password_url(self):
        driver = webdriver.Chrome()
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(*RegistrationPageLocators.LOGIN_REDIRECT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        login(driver)
        profile_link = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
        assert profile_link.is_displayed(), "Тест пройден, пользователь вошел в личный кабинет"

        driver.quit()
