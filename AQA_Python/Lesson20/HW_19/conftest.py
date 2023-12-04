import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://magento.softwaretestingboard.com/')
    yield driver
    driver.close()


@pytest.fixture()
def incognito():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://magento.softwaretestingboard.com/')
    return driver
#
#
# @pytest.fixture()
# def headless():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get('https://magento.softwaretestingboard.com/')
#     return driver
