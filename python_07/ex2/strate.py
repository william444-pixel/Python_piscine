from abc import abstractmethod, ABC
from ex0 import models as mod
from ex1 import modules as mud
from typing import Any


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: mod.Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: mod.Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: mod.Creature) -> bool:
        return True

    def act(self, creature: mod.Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: mod.Creature) -> bool:
        if isinstance(creature, mud.TransformCapability):
            return True
        return False

    def act(self, creature: mod.Creature) -> str:
        if self.is_valid(creature) is False:
            raise InvalidStrategyError(f"Battle error, aborting tournament: \
Invalid Creature '{creature.name}' for this aggressive strategy")
        c: Any = creature
        s1 = c.transform()
        s2 = c.attack()
        s3 = c.revert()
        return f"{s1}\n{s2}\n{s3}"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: mod.Creature) -> bool:
        if isinstance(creature, mud.HealCapability):
            return True
        return False

    def act(self, creature: mod.Creature) -> str:
        if self.is_valid(creature) is False:
            raise InvalidStrategyError(f"Battle error, aborting tournament: \
Invalid Creature '{creature.name}' for this defensive strategy")
        c: Any = creature
        s2 = c.attack()
        s3 = c.heal()
        return f"{s2}\n{s3}"
