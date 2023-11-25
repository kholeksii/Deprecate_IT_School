from selenium.webdriver.common.by import By

def test_url_after_menu_clicking(headless):
    headless.find_element(By.XPATH, '//*[@id="menu"]/ul/li[1]/a').click()
    assert headless.current_url == 'https://the-internet.herokuapp.com/floating_menu#home'

def test_url_after_news_clicking(headless):
    headless.find_element(By.XPATH, '//*[@id="menu"]/ul/li[2]/a').click()
    assert headless.current_url == 'https://the-internet.herokuapp.com/floating_menu#news'

def test_url_after_contact_clicking(headless):
    headless.find_element(By.XPATH, '//*[@id="menu"]/ul/li[3]/a').click()
    assert headless.current_url == 'https://the-internet.herokuapp.com/floating_menu#contact'

def test_url_after_about_clicking(headless):
    headless.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]/a').click()
    assert headless.current_url == 'https://the-internet.herokuapp.com/floating_menu#about'
