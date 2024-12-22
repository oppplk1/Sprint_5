from selenium import webdriver
from data import BASE_URL
from locators import MainPageLocators


class TestSections:
    def test_bun_navigation(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        bun = driver.find_element(*MainPageLocators.BUN_1)
        assert "Флюоресцентная булка R2-D3" in bun.text, "Тест пройден, секция Булки работает"
        driver.quit()

    def test_sauce_navigation(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        sauce = driver.find_element(*MainPageLocators.SAUCE_1)
        assert "Соус Spicy-X" in sauce.text, "Тест пройден, секция Соус работает"
        driver.quit()

    def test_filling_navigation(self):
        driver = webdriver.Chrome()
        driver.get(BASE_URL)

        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()
        filling = driver.find_element(*MainPageLocators.FILLING_1)
        assert "Мясо бессмертных моллюсков Protostomia" in filling.text, "Тест пройден, секция Начинки работает"
        driver.quit()
