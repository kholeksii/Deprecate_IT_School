entered_number = int(input('Enter the number of petal(integer only): '))

flower_tuple = ("I love you", "a little", "a lot", "passionately", "madly", "not at all")
number_of_petals = len(flower_tuple)

if entered_number <= 0:
    print('Incorrect value!')
elif entered_number <= number_of_petals:
    print(flower_tuple[entered_number-1])
else:
    print(flower_tuple[entered_number % number_of_petals-1])
