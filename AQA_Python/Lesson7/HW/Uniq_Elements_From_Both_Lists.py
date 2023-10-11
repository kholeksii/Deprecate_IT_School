first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

first_set = set(first_list)
second_set = set(second_list)

set_of_unique_elements = first_set.intersection(second_set)

print(f'The List of the common elements: {list(set_of_unique_elements)}')