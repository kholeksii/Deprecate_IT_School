family = {
    'grandpa': ('Alex', 76),
    'grandma': ('Nona', 74),
    'dad': ('Greg', 48),
    'mom': ('July', 45),
    'son_older': ('Bob', 18),
    'son_middle': ('Alex', 15),
    'son_young': ('Mark', 10)
}

lst_1 = []

for a, b in family.values():
    lst_1.append(b)

sorted(lst_1)

print(f'The difference between the oldest and the younges: {lst_1[0]-lst_1[-1]} years')
