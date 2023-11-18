from Mammals import Mammals
from CustomAnimals import Animals
from Predators import Predators

Dragon = Animals('Whitetooth', 3, 20, 500.1, 'grass')
Gorilla = Mammals('Glass', 27, 500.1, False)

Leopard = Predators('Speed', 4, 12, 32.1)

print(Dragon.isanimalwalkstandingup())
print(Dragon.whatanimaleats())

print(Gorilla.is_right_age())
print(Gorilla.is_human())

print(Leopard.is_big_predator())