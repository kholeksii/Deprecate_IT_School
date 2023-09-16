n = int(input('Скільки школярів? '))
k = int(input('Скільки є яблук? '))

forEachN = k//n
remainingApples = k%n

print('Стільки яблук дістанеться кожному школяру: ' + str(forEachN))
print('А стільки залишиться в кошику: ' + str(remainingApples))

