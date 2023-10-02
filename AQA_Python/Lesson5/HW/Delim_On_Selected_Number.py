selected_number = int(input("Enter the number for delim: "))

main_list = []
for number in range(1,81):
    main_list.append(number)
for element in main_list:
    if element % selected_number == 0:
        print(f'The {element} can be delimed by {selected_number}')
