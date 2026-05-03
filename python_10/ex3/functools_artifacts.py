from functools import reduce, lru_cache, partial, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "sum": operator.add,
        "multiply": operator.mul,
        "power": operator.pow,
        "max": max
    }
    if not spells or operation not in ops:
        raise Exception("empty list or false operation")
    result = reduce(ops[operation], spells)  # type: ignore
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    a = partial(base_enchantment, power=50, element="fireball")
    b = partial(base_enchantment, power=50, element="zip")
    c = partial(base_enchantment, power=50, element="rocket")
    return {
        "fire": a,
        "zip": b,
        "rocket": c}


def base_en(power: int, element: str, target: str) -> str:
    return f"{element} shoots {target} with {power} puissance"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def base(spell: Any):
    return "Unknon spell type"


@base.register(str)
def _(Enchantment: str):
    return f"Enchantment: {Enchantment}"


@base.register(int)
def _(Damagespell: int):
    return f"Damage spell: {Damagespell} damage"


@base.register(list)
def _(multi_cast: list):
    n = len(multi_cast)
    return f"Multi-cast: {n} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    return base


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    try:
        sum = spell_reducer([10, 20, 40, 30], "sum")
        print("Sum:", sum)
        maxi = spell_reducer([10, 20, 40, 30], "max")
        print("Max:", maxi)
    except Exception as e:
        print(e)
    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_en)
    func = ["fire", "zip", "rocket"]
    for a in func:
        print(enchantments[a](target="Monster"))
    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0), end="\n")
    print("Fib(1):", memoized_fibonacci(1), end="\n")
    print("Fib(10):", memoized_fibonacci(10), end="\n")
    print("Fib(15):", memoized_fibonacci(15), end="\n")
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher(["fireball", "zip", "rocket"]))
    print(dispatcher(3.14))
