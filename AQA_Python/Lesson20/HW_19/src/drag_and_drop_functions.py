import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def drag_and_drop(url, element_1_xpath, element_2_xpath, screenshot_path):
    driver = webdriver.Chrome()
    # driver.get('https://the-internet.herokuapp.com/drag_and_drop')
    #
    # drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-a"]')))
    # drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-b"]')))
    # ActionChains(driver).drag_and_drop(drag, drop).perform()
    driver.get(url)

    drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_1_xpath)))
    drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_2_xpath)))
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    driver.save_screenshot(screenshot_path)
    time.sleep(1)
    return screenshot_path


def validate_file_contents(file1, file2):
    with open(file1, 'r', errors='ignore') as f1, open(file2, 'r', errors='ignore') as f2:
        contents1 = f1.read()
        contents2 = f2.read()
    return contents1 == contents2
