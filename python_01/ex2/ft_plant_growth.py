class Plant:
    """Blueprint"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    """print_attributes"""
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
Sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
garden = [rose, Sunflower, cactus]


def print_info():
    day = 1
    print(f"=== Day {day} ===")
    for plant in garden:
        plant.get_info()
    while day < 7:
        for plant in garden:
            plant.grow()
            plant.age_up()
        day += 1
    print(f"=== Day {day} ===")
    for plant in garden:
        plant.get_info()
    print(f"Growth this week: +{day - 1}cm")


print_info()
