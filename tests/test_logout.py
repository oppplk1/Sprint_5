from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import LOGIN_URL, ACCOUNT_PROFILE_URL
from locators import MainPageLocators, PersonalAccountPageLocators
from helpers import login


class TestLogout:
    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))

        driver.find_element(*PersonalAccountPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(LOGIN_URL))
        assert driver.current_url == LOGIN_URL, "Тест пройден, выход из Личного Кабинета работает"

        driver.quit()
