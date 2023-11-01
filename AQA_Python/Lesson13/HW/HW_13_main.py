from HW_13_Utils import search_in_example, search_urls_example_by_itter, search_in_data, search_in_example_group

#for 1 task
search_in_example("abc", '1. Find "abc" in example file')

#for 2 task
search_in_example("\d\d\d.\d\d\d.\d\d\d\d", '\n2. Find phone numbers in example file')

#for 3 task
search_in_data("\d{3}.\d{3}.\d{4}", '\n3. Find phone numbers in data file')

#for 4 task
search_in_data("[8-9]00.\d{3}.\d{4}", '\n4. Find phone "800-900" numbers in data file')

#for 5 task
search_in_example_group("(Mr)\.?\s[A-Z]\w*", '\n5. Find "Mr" in example file')

#for 6 task
search_in_data("\w+@\w+\.\w+", '\n6. Find emails in data file')

#for 7 task
search_urls_example_by_itter("(www\.)?(\w+)(\.\w+)", '\n7. Find urls in example file')