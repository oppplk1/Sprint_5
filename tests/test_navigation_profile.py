from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import LOGIN_URL, ACCOUNT_PROFILE_URL
from locators import MainPageLocators
from helpers import login


class TestNavigation:
    def test_navigation_profile(self):
        driver = webdriver.Chrome()
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))
        assert driver.current_url == ACCOUNT_PROFILE_URL, "Тест пройден, успешный переход на страницу Личный Кабинет"
        driver.quit()
