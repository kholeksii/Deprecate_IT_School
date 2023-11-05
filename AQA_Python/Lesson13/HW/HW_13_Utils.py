import re


def search_by_pattern(regExp_example, text_message, text: str) -> list:
    print(f'{text_message}')
    pattern = re.compile(regExp_example)
    return pattern.findall(text)


def search_by_pattern_using_group(regExp_example, text_message, text: str) -> list:
    print(f'{text_message}')
    pattern = re.compile(regExp_example)
    matchers = pattern.finditer(text)
    return [el.group() for el in matchers]


def search_urls_example(regExp_example, text_message, text: str) -> str:
    print(f'{text_message}')

    pattern = re.compile(regExp_example)
    new_urls = pattern.sub(r'\2\3', text)
    return new_urls


def search_in_file(regExp_example, text_message, file_name) -> list:
    print(f'{text_message}')
    pattern = re.compile(regExp_example)

    with open(file_name, 'r') as file:
        content = file.read()
        return pattern.findall(content)
