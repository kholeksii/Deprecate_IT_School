def custom_square():
    for el in range(0, 1000000000, 2):
        yield el**2


gen = custom_square()

for i in gen:
    print(next(gen))