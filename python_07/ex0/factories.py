from abc import ABC, abstractmethod
from .models import Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling("Flameling", "Fire")

    def create_evolved(self):
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub("Aquabub", "Water")

    def create_evolved(self):
        return Torragon("Torragon", "Water")
