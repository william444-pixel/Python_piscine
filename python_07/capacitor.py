from ex1.factories import HealingCreatureFactory, TransformingCreatureFactory


def test_healing():
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    # Base
    base = factory.create_base()
    print(f" base:\n{base.describe()}\n{base.attack()}\n{base.heal()}")

    # Evolved
    evolved = factory.create_evolved()
    print(f" evolved:\n{evolved.describe()}\
        \n{evolved.attack()}\n{evolved.heal()}")


def test_transforming():
    print("\nTesting Creature with transform capability")
    factory = TransformingCreatureFactory()

    # Base (Shiftling)
    base = factory.create_base()
    print(f" base:\n{base.describe()}\n{base.attack()}")
    print(base.transform())
    print(base.attack())
    print(base.revert())

    # Evolved (Morphagon)
    evolved = factory.create_evolved()
    print(f" evolved:\n{evolved.describe()}\n{evolved.attack()}")
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    test_healing()
    test_transforming()
