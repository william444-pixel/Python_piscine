from ex0 import FlameFactory, AquaFactory


def battle(creature1, creature2):
    print(f"{creature1.describe()}\n vs. \n{creature2.describe()}")
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())
    print("\nTesting factory")
    test_factory(AquaFactory())
    print("\nTesting battle")

flame_fact = FlameFactory()
aqua_fact = AquaFactory()

c1 = flame_fact.create_base()
c2 = aqua_fact.create_base()

battle(c1, c2)
