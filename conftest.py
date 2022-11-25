import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"


