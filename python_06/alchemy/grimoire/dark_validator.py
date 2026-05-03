
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(ing.lower() in ingredients.lower() for ing in allowed)
    return f"{ingredients} - {'VALID' if is_valid else 'INVALID'}"
