from ex0.factories import CreatureFactory
from .modules import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformingCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Dark")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
