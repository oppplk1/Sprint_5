from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import LOGIN_URL, ACCOUNT_PROFILE_URL
from locators import MainPageLocators
from helpers import login


class TestNavigationConstructor:
    def test_navigation_constructor(self):
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
        burger_heading = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        assert 'Соберите бургер' in burger_heading.text, "Тест пройден, успешный переход в Конструктор"

        driver.quit()

    def test_navigation_logo(self):
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))

        driver.find_element(*MainPageLocators.LOGO_LINK).click()
        burger_heading = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        assert 'Соберите бургер' in burger_heading.text, "Тест пройден, успешный переход в Конструктор"

        driver.quit()
