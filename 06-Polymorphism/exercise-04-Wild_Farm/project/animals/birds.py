from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed

class Owl(Bird):
    GROWTH = 0.25

    def __init__(self, name, weight,  wing_size):
        super().__init__(name, weight,  wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(Owl.GROWTH, food)

class Hen(Bird):
    GROWTH = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight,  wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(Hen.GROWTH, food)

