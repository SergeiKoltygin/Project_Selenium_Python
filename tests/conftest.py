import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

"""
Фикстура для инициализации и завершения работы Chrome WebDriver.

:return: Экземпляр WebDriver
Автор: Колтыгин Сергей
"""
@pytest.fixture(scope="session")
def chromedriver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()