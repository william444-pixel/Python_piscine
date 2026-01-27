class Plant:
    """Blueprint"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height_new):
        if height_new > 0:
            self.__height = height_new
        else:
            self.__height = 0
            print("Invalid operation attempted: height "
                  f"{height_new}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age_new):
        if age_new > 0:
            self.__age = age_new
        else:
            print("Invalid operation attempted:"
                  f"age {age_new} days [REJECTED]")
            print("Security: Negative age rejected")

    """print_attributes"""
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


def main():
    rose = Plant("Rose", -25, 30)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"age updated: {rose.get_age()} days [OK]\n")
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


main()
