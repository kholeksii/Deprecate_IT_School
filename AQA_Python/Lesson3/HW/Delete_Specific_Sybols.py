enteredString = input('Enter the STRING, please: ')
selectedSymbol = input('Enter the symbol which need to be deleted: ')

result = enteredString.replace(selectedSymbol.lower(),'').replace(selectedSymbol.capitalize(),'')
print(f'The cleared string: \n {result}')
