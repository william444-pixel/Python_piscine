from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_got(target: str, power: int):
    return power > 50


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


print("\nTesting spell combiner...")
comb = spell_combiner(heal, fireball)
print(*comb("dragon", 3))
print("\nTesting power amplifier...")
amp = power_amplifier(fireball, 5)
print(amp("dragon", 5))
print("\nTesting conditional caster...")
cd = conditional_caster(is_got, fireball)
print(cd("monster", 55))
print(cd("monster", 30))
print("\nTesting spell sequence...")
ss = spell_sequence([fireball, heal])
print(ss("prince", 10))
