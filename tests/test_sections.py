from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import BASE_URL
from locators import MainPageLocators


class TestSections:
    def test_bun_navigation(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCE_1))
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()
        bun = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUN_1))
        assert "Флюоресцентная булка R2-D3" in bun.text

    def test_sauce_navigation(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        sauce = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCE_1))
        assert "Соус Spicy-X" in sauce.text

    def test_filling_navigation(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()
        filling = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FILLING_1))
        assert "Мясо бессмертных моллюсков Protostomia" in filling.text
