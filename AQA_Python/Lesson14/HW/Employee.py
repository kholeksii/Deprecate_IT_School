import time


class Employer:
    employer_id = 1

    def __init__(self, name: str, last_name: str, age: int, sex: str, marital_status: str, position: str,
                 start_working_year: int, end_working_day=None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.marital_status = marital_status
        self.position = position
        self.start_working_year = start_working_year
        self.end_working_day = end_working_day
        self.employer_id = Employer.id_counter()

    def welcome(self):
        print(f'Welcome, dear {self.name} {self.last_name}! ')

    def employer_age(self):
        print(f'{self.name} {self.last_name} is {self.age} years old.')

    def employer_sex(self):
        print(f'{self.name} {self.last_name} is {self.sex}. And {self.marital_status}. ')

    def id_employer(self):
        print(f'{self.name} {self.last_name} has ID# {self.employer_id}.')

    def employer_working_position(self):
        experience = int(time.strftime("%Y")) - self.start_working_year
        print(f'Employer {self.name} {self.last_name} has {self.position} and works from {self.start_working_year} '
              f'that means has {experience} year(s) of experience')


    @classmethod
    def id_counter(cls):
        cls.employer_id += 1
        return cls.employer_id


Oleksii = Employer('Oleksii', 'Kharchenko', 32, 'male', 'married', 'Junior QA', 2021)
Hanna = Employer('Hanna', 'Sternenko', 26, 'male', 'married', 'Junior UI/UX Designer', 2022)

Oleksii.welcome()
Oleksii.employer_age()
Oleksii.employer_sex()
Oleksii.employer_working_position()
Oleksii.id_employer()

Hanna.welcome()
Hanna.employer_age()
Hanna.employer_sex()
Hanna.employer_working_position()
Hanna.id_employer()