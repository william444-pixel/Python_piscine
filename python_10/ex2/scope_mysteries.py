from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    i = initial_power

    def accmultor(amount: int):
        nonlocal i
        i += amount
        return i
    return accmultor


def enchantment_factory(enchantment_type: str) -> Callable:
    type = enchantment_type

    def result(item_name):
        return f"{type} {item_name}"
    return result


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


print("Testing mage counter...")
ca = mage_counter()
cb = mage_counter()
print("counter_a call 1:", ca())
print("counter_a call 2:", ca())
print("counter_b call 3:", cb())
print("\nTesting spell accumulator...")
sa = spell_accumulator(100)
print(f"base 100, add 20: {sa(20)}")
print(f"base 100, add 30: {sa(30)}")
print("\nTesting enchantment factory...")
a = enchantment_factory("Flamling")
print(a("Sword"))
b = enchantment_factory("Frozen")
print(a("Shield"))
print("\nTesting memory vault...")
vault = memory_vault()
vault["store"]("secret", 42)
print("Store 'secret' = 42")
print("Recall 'secret':", vault["recall"]("secret"))
print("Recall 'unknown':", vault["recall"]("wrong_key"))
