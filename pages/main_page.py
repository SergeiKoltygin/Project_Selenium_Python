import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.google_search_results_page import GoogleSearchResultsPage

"""
Инициализация главной страницы Google.

:param driver: Экземпляр веб-драйвера
Автор: Колтыгин Сергей
"""
class GooglMainPage:
    def __init__(self, driver):

        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.driver.get("https://www.google.com")

        """
        Выполняет поиск по введённому запросу.

        :param query: Строка поискового запроса
        :return: Экземпляр GoogleSearchResultsPage
        Автор: Колтыгин Сергей
        """
    @allure.step("Ввод запроса в строку поиска")
    def search_for(self, query):
        search_input = self.driver.find_element(*self.search_box)
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
        return GoogleSearchResultsPage(self.driver)