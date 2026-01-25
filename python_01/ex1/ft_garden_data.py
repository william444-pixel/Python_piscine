class Plant:
    """Blueprint"""
    def __init__(self, name: str, height: str, age: str):
        self.name = name
        self.height = height
        self.age = age

    """print_attributes"""
    def print(self):
        print(f"{self.name}: {self.height}, {self.age}")


rose = Plant("Rose", "25cm", "30 days old")
Sunflower = Plant("Sunflower", "80cm", "45 days old")
cactus = Plant("Cactus", "15cm", "120 days old")
print("=== Garden Plant Registry ===")
rose.print()
Sunflower.print()
cactus.print()
