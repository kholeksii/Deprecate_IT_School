def collect_values():
    value_1 = input('Enter the first value: ')
    value_2 = input('Enter the second value: ')
    operation = input('Which operation do you want to do? +, -, *, /')

    return value_1, value_2, operation


def calc_values(number_1, number_2, operation):
    if operation == '+':
        return float(number_1) + float(number_2)
    if operation == '-':
        return float(number_1) - float(number_2)
    if operation == '*':
        return float(number_1) * float(number_2)
    if operation == '/':
        return float(number_1) / float(number_2)
    else:
        return 'Not known operation'


print(calc_values(*(collect_values())))
