import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/floating_menu')
    yield driver
    driver.close()


@pytest.fixture()
def incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://the-internet.herokuapp.com/floating_menu')
    return driver


@pytest.fixture()
def headless():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://the-internet.herokuapp.com/floating_menu')
    return driver
