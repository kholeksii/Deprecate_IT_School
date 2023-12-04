from src.find_elements import *

def test_url_women_top_1(incognito):
    received_url=find_submenu_item(incognito,'Women', 'Tops', 'Jackets')
    assert received_url == 'https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html'

def test_url_women_top_2(incognito):
    received_url=find_submenu_item(incognito,'Women', 'Tops', 'Hoodies & Sweatshirts')
    assert received_url == 'https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html'

def test_url_women_top_3(incognito):
    received_url = find_submenu_item(incognito, 'Women', 'Tops', 'Tees')
    assert received_url == 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'

def test_url_women_top_4(incognito):
    received_url = find_submenu_item(incognito, 'Women', 'Tops', 'Bras & Tanks')
    assert received_url == 'https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html'

def test_url_women_bottoms_1(incognito):
    received_url = find_submenu_item(incognito, 'Women', 'Bottom', 'Pants')
    assert received_url == 'https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html'

def test_url_women_bottoms_2(incognito):
    received_url = find_submenu_item(incognito, 'Women', 'Bottom', 'Shorts')
    assert received_url == 'https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html'