
def collect_the_number():
    entered_number = int(input('Enter the number for verification(between 2 and 1000): '))
    return entered_number


def is_prime_number(entered_number):
    if 1 < entered_number < 1000:
        for i in range(2, entered_number):
            if entered_number % i == 0:
                print(f'{entered_number} is not a prime number')
                break
        else:
            print(f'{entered_number} is a prime number')
    else:
        print('Incorrect value has been entered')


is_prime_number(collect_the_number())
