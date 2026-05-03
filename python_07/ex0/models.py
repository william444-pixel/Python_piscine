from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def attack(self):
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self):
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self):
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self):
        return "Torragon uses Hydro Pump!"
