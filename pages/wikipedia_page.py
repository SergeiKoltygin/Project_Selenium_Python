import allure
from selenium.webdriver.common.by import By

"""
Инициализация страницы Википедии.

:param driver: Экземпляр веб-драйвера
Автор: Колтыгин Сергей
"""
class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.header = (By.TAG_NAME, "h1")
        self.author_info = (By.XPATH, "//th[text()='Автор']/following-sibling::td")

        """
        Проверяет, соответствует ли автор страницы ожидаемому.

        :param expected_author: Ожидаемое имя автора
        :return: True, если автор найден, иначе False
        Автор: Колтыгин Сергей
        """
    @allure.step("Проверка автора страницы")
    def check_author(self, expected_author):
        author = self.driver.find_element(*self.author_info).text
        return expected_author in author
