from HW_13_Utils import search_by_pattern, search_urls_example, search_in_file, search_by_pattern_using_group
from examples import text_to_search, urls


#for 1 task
print(search_by_pattern("abc", '1. Find "abc" in example file', text_to_search))

#for 2 task
print(search_by_pattern("\d\d\d.\d\d\d.\d\d\d\d", '\n2. Find phone numbers in example file', text_to_search))

#for 3 task
print(search_in_file("\d{3}.\d{3}.\d{4}", '\n3. Find phone numbers in data file', 'data.txt'))

#for 4 task
print(search_in_file("[8-9]00.\d{3}.\d{4}", '\n4. Find phone "800-900" numbers in data file', 'data.txt'))

#for 5 task
print(search_by_pattern_using_group("(Mr)\.?\s[A-Z]\w*", '\n5. Find "Mr" in example file', text_to_search))

#for 6 task
print(search_in_file("\w+@\w+\.\w+", '\n6. Find emails in data file', 'data.txt'))

#for 7 task
print(search_urls_example("https?://(www\.)?(\w+)(\.\w+)", '\n7. Find urls in example file', urls))