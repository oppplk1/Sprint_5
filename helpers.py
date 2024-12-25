import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import VALID_EMAIL, VALID_PASSWORD
from locators import LoginPageLocators, MainPageLocators


def login(driver):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER))


def generate_unique_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=7))
    return f"{username}@yandex.ru"
