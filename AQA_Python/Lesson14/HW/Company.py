import time
class Company:
    def __init__(self, name:str, since:int, employees_number:int):
        self.name = name
        self.since = since
        self.employees_number = employees_number

    def welcome(self):
        print(f'Welcome to {self.name} company! ')

    def age(self):
        year = int(time.strftime("%Y"))
        age = year - self.since
        print(f'The {self.name} Company was found in {self.since}, that means the Company works more than {age} years. ')

    def employees(self):
        print(f'The {self.name} Company grew from a small garage to a staff of {self.employees_number} employees. ')

Apple = Company('Apple', 1976, 80000)
Toshiba = Company('Toshiba', 1875, 116000)

Apple.welcome()
Apple.age()
Apple.employees()

Toshiba.welcome()
Toshiba.age()
Toshiba.employees()