from ex0 import factories as f0
from ex1 import factories as f1
from ex2 import strate


def battle(opponents_data):

    fighters = []
    for c, s in opponents_data:
        fighters.append((c, s))
    print(f"{len(fighters)} opponents involved")

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            c1, s1 = fighters[i]
            c2, s2 = fighters[j]
            print("\n* Battle *")
            print(f"{c1.describe()}\n vs.\n{c2.describe()}")
            print(" now fight!")
            try:
                print(s1.act(c1))
                print(s2.act(c2))
            except strate.InvalidStrategyError as e:
                print(e)
                return


if __name__ == "__main__":
    opponents = [
        (f0.FlameFactory().create_base(), strate.NormalStrategy()),
        (f1.HealingCreatureFactory().create_base(), strate.DefensiveStrategy())
    ]

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ] \n*** Tournament ***")
    battle(opponents)
    opponents = [
        (f0.FlameFactory().create_base(), strate.AggressiveStrategy()),
        (f1.HealingCreatureFactory().create_base(), strate.DefensiveStrategy())
    ]
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]"
          "\n*** Tournament ***")
    battle(opponents)
    opponents = [
        (f0.AquaFactory().create_base(), strate.NormalStrategy()),
        (f1.HealingCreatureFactory().create_base(),
         strate.DefensiveStrategy()),
        (f1.TransformingCreatureFactory().create_base(),
         strate.AggressiveStrategy())
    ]
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
          "\n*** Tournament ***")
    battle(opponents)
