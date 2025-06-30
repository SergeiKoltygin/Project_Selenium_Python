import allure
import pytest

from config.config import google_url
from pages import main_page

"""
Фикстура для запуска тестов: открывает главную страницу Google.

:param chromedriver: Инициализированный WebDriver
:return: WebDriver
Автор: Колтыгин Сергей
"""
@pytest.fixture(scope="session")
def setup(chromedriver):
    chromedriver.get(google_url)
    return chromedriver

@pytest.mark.parametrize(
    "search_query, expected_author",
    [
        ("Python википедия", "Гвидо ван Россум"),
    ]
)
@allure.title("Тестирование поиска Python в Google")

def test_wikipedia_author_in_search_results(setup, search_query, expected_author):
    """
    Тест проверяет, что при поиске Python в Google среди результатов есть статья Википедии
    с нужным автором.

    :param setup: WebDriver
    :param search_query: Поисковый запрос
    :param expected_author: Ожидаемое имя автора
    Автор: Колтыгин Сергей
    """
    driver = setup
    google_home = main_page.GooglMainPage(driver)
    search_results = google_home.search_for(search_query)
    wiki_page = search_results.open_first_result()
    assert wiki_page.check_author(expected_author), f"Автор в Википедии не {expected_author}"
