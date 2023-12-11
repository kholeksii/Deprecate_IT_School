from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MySelenium:
    def __init__(self, browser_type="chrome"):
        self.browser_type=browser_type
        self.driver= self._get_driver()

    def _get_driver(self):
        if self.browser_type == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_type == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

        return driver

    def get_page(self, url):
        self.driver.get(url)

    def search_box(self, text):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
        element.clear()
        element.send_keys(text)
        return element.get_attribute("value")


    def redirect(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
        element.clear()
        element.send_keys("test")
        element.send_keys(Keys.RETURN)
        return self.driver.current_url

    def get_current_url(self):
        return self.driver.current_url

    def get_all_urls_with_tag(self, base_url, tag):
        links_list = self.driver.find_elements(By.TAG_NAME, tag)
        link_url_list = []
        for link in links_list:
            link_url = link.get_attribute('href')
            if link_url and link_url.startswith('http'):
                link_url_list.append(link_url)
        i=0
        for url in link_url_list:
            self.driver.get(url)
            self.driver.save_screenshot(f'Scr_{i}.png')
            self.driver.back()
            i=i+1

        self.driver.get(base_url)
        return len(link_url_list)

    def close_browser(self):
        self.driver.quit()
        