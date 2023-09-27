lst_1 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
print(f'The origin list: {lst_1}')
print(f'Is the list sorted correctly? -- {lst_1==sorted(lst_1, key=str.lower)}')
print(f'The sorted list should be: {sorted(lst_1, key=str.lower)}')