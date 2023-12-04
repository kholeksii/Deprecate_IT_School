from src.find_elements import *

def test_url_men_top_1(incognito):
    received_url=find_submenu_item(incognito,'Men', 'Tops', 'Jackets')
    assert received_url == 'https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html'

def test_url_men_top_2(incognito):
    received_url=find_submenu_item(incognito,'Men', 'Tops', 'Hoodies & Sweatshirts')
    assert received_url == 'https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html'

def test_url_men_top_3(incognito):
    received_url = find_submenu_item(incognito, 'Men', 'Tops', 'Tees')
    assert received_url == 'https://magento.softwaretestingboard.com/men/tops-men/tees-men.html'

def test_url_men_top_4(incognito):
    received_url = find_submenu_item(incognito, 'Men', 'Tops', 'Tanks')
    assert received_url == 'https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html'

def test_url_men_bottoms_1(incognito):
    received_url = find_submenu_item(incognito, 'Men', 'Bottom', 'Pants')
    assert received_url == 'https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html'

def test_url_men_bottoms_2(incognito):
    received_url = find_submenu_item(incognito, 'Men', 'Bottom', 'Shorts')
    assert received_url == 'https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html'