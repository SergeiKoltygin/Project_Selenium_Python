import allure
from selenium.webdriver.common.by import By

from pages.wikipedia_page import WikipediaPage

"""
Инициализация страницы результатов поиска Google.

:param driver: Экземпляр веб-драйвера
Автор: Колтыгин Сергей
"""
class GoogleSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wik_result = (By.XPATH, '//a[contains(@href, "ru.wikipedia.org/wiki/Python") and .//h3[contains(text(), "Python")]]')

        """
        Открывает ссылку из результатов поиска.

        :return: Экземпляр WikipediaPage
        Автор: Колтыгин Сергей
        """
    @allure.step("Открыть первую страницу результата")
    def open_first_result(self):
        results = self.driver.find_elements(By.XPATH, '//h3')
        assert len(results) > 0, "Результаты поиска не отображаются на странице"
        self.driver.find_element(*self.wik_result).click()
        return WikipediaPage(self.driver)