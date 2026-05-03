
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    p_sorted = sorted(artifacts, key=lambda a: a["power"], reverse=True)
    return p_sorted


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = filter(lambda mage: mage["power"] >= min_power, mages)
    return list(result)


def spell_transformer(spells: list[str]) -> list[str]:
    rus = map(lambda s: "*" + s + "*", spells)  # noqa: C417
    return list(rus)


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": (lambda mage: max([i["power"] for i in mage]))(mages),
            "min_power": (lambda mage: min([i["power"] for i in mage]))(mages),
            "avg_power": (lambda mage:
                          round(sum([i["power"] for i in mage])
                                / len([i["power"] for i in mage]), 2))(mages)}


if __name__ == "__main__":
    artifacts = [{'name': 'Light Prism', 'power': 118, 'type': 'focus'},
                 {'name': 'Water Chalice', 'power': 83, 'type': 'focus'},
                 {'name': 'Ice Wand', 'power': 93, 'type': 'armor'},
                 {'name': 'Lightning Rod', 'power': 61, 'type': 'armor'}]
    print("\nTesting artifact sorter...")
    a = artifact_sorter(artifacts)
    print(f"{a[0]['name']} ({a[0]['power']} power) comes before", end=" ")
    print(f"{a[1]['name']} ({a[1]['power']} power)\n")
    print("\nTesting power filter...")
    p = power_filter(artifacts, 90)
    print("dict of power up then 90:", *p)
    spells = ['fireball', 'earthquake', 'shield', 'freeze']
    spells_tr = spell_transformer(spells)
    print("\nTesting spell transformer...")
    for sp in spells_tr:
        print(sp, end=" ")
    print("\n \nTesting mage state...")
    m = mage_stats(artifacts)
    print(m)
