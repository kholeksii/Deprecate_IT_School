lst_1 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
print(f'The Original List :{lst_1}')
lst_1.sort(reverse=False, key=str.lower)
print(f'The Sorted List :{lst_1}')