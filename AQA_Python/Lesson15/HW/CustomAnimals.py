class Animals:
    def __init__(self, name: str, legs: int, age: int, weight: float, eat: str):
        self._name = name
        self._legs = legs
        self.__age = age
        self.__weight = weight
        self._eat = eat

    def __str__(self) -> object:
        return f'The Animal {self._name} has {self._legs} legs and {self.__age} years old'

    @property
    def name(self):
        return self._name

    @property
    def legs(self):
        return self._legs

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @name.setter
    def name(self, value):
        self._name = value

    @legs.setter
    def legs(self, value):
        self._legs = value

    @age.setter
    def age(self, value):
        self.__age = value

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def isanimalwalkstandingup(self) -> object:
        if self._legs < 4:
            return f'{self.name} is walk standing up!'

    def whatanimaleats(self):
        return f'{self.name} eats {self._eat}!'