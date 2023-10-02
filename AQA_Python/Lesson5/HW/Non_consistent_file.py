main_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]

for element in main_list:
    idx = main_list.index(element)
    if idx != 0 and element-main_list[idx-1] != 1:
        print(f'The element {element} is not consistent')
        break
