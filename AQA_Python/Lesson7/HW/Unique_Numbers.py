entered_digits = input('Please, enter the digits list, separated by space: ')

print(f'Does the entered list contain the unique digits only? -- {len(set(entered_digits.split()))==len(entered_digits.split())}')
