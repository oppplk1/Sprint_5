from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import VALID_EMAIL, VALID_PASSWORD
from locators import LoginPageLocators


def login(driver):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
