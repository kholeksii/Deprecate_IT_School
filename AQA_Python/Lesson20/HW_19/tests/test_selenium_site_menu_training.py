from src.find_elements import *

def test_url_training_top_1(incognito):
    received_url=find_submenu(incognito,'Training', 'Video Download')
    assert received_url == 'https://magento.softwaretestingboard.com/training/training-video.html'
