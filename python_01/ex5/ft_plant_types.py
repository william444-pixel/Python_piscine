class Plant:
    """Blueprint"""
    def __init__(self, name: str, height: str, age: str):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def print_info(self):
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self. trunk_diameter = trunk_diameter

    def print_info(self):
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        print(f"{self.name} provides 78 square meteres of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age,  harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def value(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def main():
    rose = Flower("Rose", 25, 30, "red")
    rose.print_info()
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    oak.print_info()
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "b")
    tomato.print_info()
    tomato.value()


main()
