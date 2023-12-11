import pytest
# from selenium_all import MySelenium
from Lesson21.CW.selenium_all import MySelenium


# @pytest.mark.parametrize('base_url', [('https://www.google.com.ua')])
# def test_base_url(base_url):
#     page = MySelenium()
#     page.get_page(base_url)
#
#     assert page.get_current_url() == 'https://www.google.com.ua/'
#
#
# @pytest.mark.parametrize('base_url, param', [('https://www.google.com.ua/', 'Hello, world!')])
# def test_search_box(base_url, param):
#     page = MySelenium()
#     page.get_page(base_url)
#     test_box = page.search_box(param)
#     assert test_box == 'Hello, world!'
#
#
# @pytest.mark.parametrize('base_url', [('https://www.google.com.ua')])
# def test_search_box_2(base_url):
#     page = MySelenium()
#     page.get_page(base_url)
#     new_url = 'https://www.google.com.ua/search?q=test&sca_esv=589455124&source=hp&ei=gO90ZYmoKZiUxc8P7bS2kAI&iflsig=AO6bgOgAAAAAZXT9kDsFQsC1yS5DxP-Fjdct3e1SN6jz&ved=0ahUKEwiJ6JTcuIODAxUYSvEDHW2aDSIQ4dUDCAo&uact=5&oq=test&gs_lp=Egdnd3Mtd2l6IgR0ZXN0SBpQAFgHcAB4AJABAJgBAKABAKoBALgBA8gBAPgBAQ&sclient=gws-wiz'
#     assert page.redirect() == new_url


@pytest.mark.parametrize('base_url, tag', [('https://www.google.com.ua', 'a')])
def test__urls_with_tag(base_url, tag):
    page = MySelenium()
    page.get_page(base_url)
    elements_count = page.get_all_urls_with_tag(base_url, tag)
    assert elements_count == 17