my_min = lambda *args: print('Enter the arguments!') if not args else sorted(args)[-1]

print(my_min(7, 2, 6, 4, 5))