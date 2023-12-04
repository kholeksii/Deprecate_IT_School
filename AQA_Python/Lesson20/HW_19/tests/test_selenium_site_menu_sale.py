from src.find_elements import *

def test_url_sale_1(incognito):
    received_url=find_menu(incognito,'Sale')
    assert received_url == 'https://magento.softwaretestingboard.com/sale.html'
