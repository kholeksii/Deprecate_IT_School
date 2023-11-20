from CustomAnimals import Animals


class Mammals(Animals):
    def __init__(self, name:str, age:int, weight:float, human:bool):
        super().__init__(name, 2, age, weight, 'grass')
        self.human = human

    def is_right_age(self) -> bool:
        if self.age > 63:
            return False
        else:
            return True

    def is_human(self) -> bool:
        if not self.human:
            return False
        else:
            return True
