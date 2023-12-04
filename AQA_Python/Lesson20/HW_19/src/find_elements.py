from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def find_submenu_item(browser, menu_title, submenu_title, submenu_item_title) -> str:
    # browser.get('https://magento.softwaretestingboard.com/')
    menu = browser.find_element(By.PARTIAL_LINK_TEXT, menu_title)
    menu.click()
    submenu = browser.find_element(By.PARTIAL_LINK_TEXT, submenu_title)
    actions = ActionChains(browser)
    submenu_item = browser.find_element(By.PARTIAL_LINK_TEXT, submenu_item_title)
    actions.move_to_element(submenu)
    actions.click(submenu_item)
    actions.perform()
    # browser.save_screenshot('screenshot'+'_'+menu_title+'_'+submenu_title+'_'+submenu_item_title+'.png')
    return browser.current_url


def find_submenu(browser, menu_title, submenu_title) -> str:
    menu = browser.find_element(By.PARTIAL_LINK_TEXT, menu_title)
    menu.click()
    submenu = browser.find_element(By.PARTIAL_LINK_TEXT, submenu_title)
    actions = ActionChains(browser)
    actions.move_to_element(submenu)
    actions.click(submenu)
    actions.perform()
    # browser.save_screenshot('screenshot'+'_'+menu_title+'_'+submenu_title+'.png')
    return browser.current_url


def find_menu(browser, menu_title) -> str:
    menu = browser.find_element(By.PARTIAL_LINK_TEXT, menu_title)
    menu.click()
    # browser.save_screenshot('screenshot'+'_'+menu_title+'.png')
    return browser.current_url
