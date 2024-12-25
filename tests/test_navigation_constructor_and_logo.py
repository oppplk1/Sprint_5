from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import LOGIN_URL, ACCOUNT_PROFILE_URL
from locators import MainPageLocators
from helpers import login


class TestNavigationConstructor:
    def test_navigation_constructor(self, driver):
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
        burger_heading = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BURGER_HEADING))
        assert 'Соберите бургер' in burger_heading.text

    def test_navigation_logo(self, driver):
        driver.get(LOGIN_URL)

        login(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(ACCOUNT_PROFILE_URL))

        driver.find_element(*MainPageLocators.LOGO_LINK).click()
        burger_heading = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BURGER_HEADING))
        assert 'Соберите бургер' in burger_heading.text
