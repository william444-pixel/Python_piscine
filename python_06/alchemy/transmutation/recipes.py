from alchemy import create_air, create_fire
from .. import potions as p


def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and \
'{p.strength_potion()}' mixed with '{create_fire()}'"
