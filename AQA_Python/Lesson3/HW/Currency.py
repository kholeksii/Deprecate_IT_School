print(
    '1 -- UAH -> USD \n'
    '2 -- USD -> UAH \n'
    '3 -- UAH -> EUR \n'
    '4 -- EUR -> UAH \n'
)
UAH = '₴'
USD = '$'
USD_value = float('38.5')
EUR = '€'
EUR_value = float('41.6')
enteredMode = int(input('Enter the number which corresponds to the convert mode: '))
enteredTheValue = int(input('Enter the number of bills: '))

if enteredMode == 1:
    result = enteredTheValue / USD_value
    print(f'{result} {USD} can you receive with currency {USD_value} {UAH} for 1 {USD}')
elif enteredMode == 2:
    result = enteredTheValue * USD_value
    print(f'{result} {UAH} can you receive with currency {USD_value} {UAH} for 1 {USD}')
elif enteredMode == 3:
    result = enteredTheValue / EUR_value
    print(f'{result} {EUR} can you receive with currency {EUR_value} {UAH} for 1 {EUR}')
elif enteredMode == 4:
    result = enteredTheValue * EUR_value
    print(f'{result} {UAH} can you receive with currency {EUR_value} {UAH} for 1 {EUR}')
else:
    print('Incorrect selected mode!')
