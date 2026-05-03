from abc import ABC, abstractmethod
import ex0.models as creature_models


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(creature_models.Creature, HealCapability):
    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(creature_models.Creature, HealCapability):
    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount!"


class Shiftling(creature_models.Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        creature_models.Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self):
        if not self.transformed:
            self.transformed = True
            return "Shiftling shifts into a sharper form!"
        else:
            return "Shiftling is already in shaper form."

    def revert(self):
        if self.transformed:
            self.transformed = False
            return "Shiftling returns to normal"
        else:
            return "shiftling is already normal"


class Morphagon(creature_models.Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        creature_models.Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self):
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally"

    def transform(self):
        if not self.transformed:
            self.transformed = True
            return "Morphagon morphs into a dragonic battle form!"
        else:
            return "Morphagon is already in dragonic Form."

    def revert(self):
        if self.transformed:
            self.transformed = False
            return "Morphagon stabilizes its form"
        else:
            return "Morphagon is already in stabilizes form."
