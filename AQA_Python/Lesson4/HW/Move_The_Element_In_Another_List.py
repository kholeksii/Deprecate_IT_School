lst_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
print(f'The Source of First List :{lst_1}')
lst_2 = []
lst_2 = lst_1[6].pop(3)
print(f'The First List :{lst_1}')
print(f'The Second List :{lst_2}')