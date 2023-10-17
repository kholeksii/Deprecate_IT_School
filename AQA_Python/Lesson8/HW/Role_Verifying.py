entered_name = input('Please, enter your name: ')

roles = {
    'admin': ['Oleksii', 'Pavlo'],
    'maintainer': ['Hanna', 'Sam'],
    'manager': ['Maryna', 'Zoe'],
    'developer': ['Alex', 'Jack']
}

entered_name = entered_name.title()
login_message = ''

for key, value in roles.items():
    if entered_name in value:
        login_message = str(f'Hello, {key}!')
        break
    else:
        login_message = str('Hello, Guest!')
        pass

print(login_message)
