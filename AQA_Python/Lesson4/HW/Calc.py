number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

operation_mode = input('Enter the operation which want to use: +, -, *, / ')

if operation_mode=='+':
    result = float(number_1 + number_2)
elif operation_mode=='-':
    result = float(number_1 - number_2)
elif operation_mode=='*':
    result = float(number_1 * number_2)
elif operation_mode == '/':
    result = float(number_1 / number_2)
else:
    result = 'The selected mode or number entered icorrect'

print(f'The result: {result}')
