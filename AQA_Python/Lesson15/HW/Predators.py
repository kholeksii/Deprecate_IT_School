from Mammals import Mammals


class Predators(Mammals):
    def __init__(self, name:str, legs:int, age:int, weight:float, human=False, eat='meat'):
        super().__init__(name, age, weight, human)
        self._eat = eat
        self._legs = legs

    def is_big_predator(self) -> bool:
        if self.weight > 100:
            return True
        else:
            return False
