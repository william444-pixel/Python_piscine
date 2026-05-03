import elements as base_el        # Fire & Water
from . import elements as local_el  # Earth & Air


def healing_potion():
    return f"Healing potion brewed with \
'{local_el.create_earth()}' and '{local_el.create_air()}'"


def strength_potion():
    return f"Strength potion brewed with \
'{base_el.create_fire()}' and '{base_el.create_water()}'"
