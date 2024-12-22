import pytest
from selenium import webdriver
from data import BASE_URL


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(BASE_URL)
    yield browser
    browser.quit()
