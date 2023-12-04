from src.find_elements import *

def test_url_gear_1(incognito):
    received_url=find_submenu(incognito,'Gear', 'Bags')
    assert received_url == 'https://magento.softwaretestingboard.com/gear/bags.html'

def test_url_gear_2(incognito):
    received_url=find_submenu(incognito,'Gear', 'Fitness Equipment')
    assert received_url == 'https://magento.softwaretestingboard.com/gear/fitness-equipment.html'

def test_url_gear_3(incognito):
    received_url = find_submenu(incognito, 'Gear', 'Watches')
    assert received_url == 'https://magento.softwaretestingboard.com/gear/watches.html'
