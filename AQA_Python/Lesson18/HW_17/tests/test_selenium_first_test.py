from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_search(browser, my_text=None):
    if my_text == None:
        my_text = 'Hillel IT School'

    browser.get("https://www.google.com")

    search_box = browser.find_element(By.ID, "APjFqb")
    search_box.send_keys("Hillel IT School")
    text = search_box.get_attribute('value')
    assert text == 'Hillel IT School'

    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    assert text in browser.title, f"Search doesn't have {text}"

    search_box2 = browser.find_element(By.ID, "APjFqb")
    text_in_result = search_box2.get_attribute('value')
    assert text_in_result == 'Hillel IT School'

    search_page_result_text = browser.find_elements(By.CSS_SELECTOR, "#search h3")
    assert any(my_text in result.text for result in search_page_result_text), f"Search Result Page doesn\'t have {my_text}"


