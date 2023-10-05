entered_number = int(input('Enter the number of petal(integer only): '))-1

flower_tuple = ("I love you", "a little", "a lot", "passionately", "madly", "not at all")

if entered_number < 0:
    print('Incorrect value!')
elif entered_number < len(flower_tuple):
    print(flower_tuple[entered_number])
else:
    print('Too big number!')
