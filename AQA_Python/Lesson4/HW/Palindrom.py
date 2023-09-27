enteredText = str(input('Type the word :'))
mirroredText = enteredText[::-1]
if enteredText == mirroredText:
    print(f'The word "{enteredText}" is palindrom')
else:
    print(f'The word "{enteredText}" is not palindrom')