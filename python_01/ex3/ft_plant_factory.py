class Plant:
    """Blueprint"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    """print_attributes"""
    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


garden = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
    ]


def print_info():
    number = 0
    print("=== Plant Factory Output ===")
    for plant in garden:
        number += 1
        plant.get_info()
    print(f"Total plants created: {number}")


print_info()
