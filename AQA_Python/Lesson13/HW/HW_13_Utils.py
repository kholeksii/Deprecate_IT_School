import re
from examples import text_to_search, urls

def search_in_example(regExp_example, text_message):
    print(f'{text_message}')
    pattern = re.compile(regExp_example)
    matchers = pattern.findall(text_to_search)
    for el in matchers:
        print(el)


def search_in_example_group(regExp_example, text_message):
    print(f'{text_message}')
    result = []
    pattern = re.compile(regExp_example)
    matchers = pattern.finditer(text_to_search)
    for el in matchers:
        result.append(el.group())
        print(el.group())


def search_urls_example_by_itter(regExp_example, text_message):
    print(f'{text_message}')
    result = []
    pattern = re.compile(regExp_example)
    new_urls = urls.replace('https?://', '')
    print(new_urls)
    matchers = pattern.finditer(new_urls)
    for el in matchers:
        result.append(el.group())
        print(el.group())


def search_in_data(regExp_example, text_message):
    print(f'{text_message}')
    pattern = re.compile(regExp_example)

    with open ('data.txt', 'r') as file:
        content = file.read()
        matchers = pattern.findall(content)
        for el in matchers:
            print(el)
