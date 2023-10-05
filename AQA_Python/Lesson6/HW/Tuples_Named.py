from collections import namedtuple

car = namedtuple('car', ['car_brand', 'car_name', 'year'])
Car1 = car('Toyota', 'Corolla', 2001)
Car2 = car('Toyota', 'Supra', 1998)
Car3 = car('Volkswagen', 'Passat', 2012)

namedtuple_list = ([Car1, Car2, Car3])
result = ''

for value in namedtuple_list:
    if type(value.car_brand) == str:
        result = f'The car brand is {value.car_brand}'
    else:
        print(f'Warning! Invalid data type. Expected "str", Actual {type(value.car_brand)}')
    if type(value.car_name) == str:
        result = result + f' {value.car_name}'
    else:
        print(f'Warning! Invalid data type. Expected "str", Actual {type(value.car_name)}')
    if type(value.year) == int:
        result = result + f', and the year is {value.year}'
    else:
        print(f'Warning! Invalid data type. Expected "int", Actual {type(value.year)}')
    print(result)


# Here is another variants:
# 1
# for value in namedtuple_list:
#     if type(value.car_brand) == str:
#         print(f'The car brand is {value.car_brand}')
#     else:
#         print(f'Warning! Invalid data type. Expected "str", Actual {type(value.car_brand)}')
#     if type(value.car_name) == str:
#         print(f'The name is {value.car_name}')
#     else:
#         print(f'Warning! Invalid data type. Expected "str", Actual {type(value.car_name)}')
#     if type(value.year) == int:
#         print(f'The year is {value.year}')
#     else:
#         print(f'Warning! Invalid data type. Expected "int", Actual {type(value.year)}')
