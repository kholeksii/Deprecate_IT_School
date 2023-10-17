information_request = input('Enter the key for information: ')

course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    print(str(course[information_request]))
except KeyError:
    print("Error! Incorrect key has been entered.")
