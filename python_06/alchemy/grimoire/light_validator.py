from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = light_spell_allowed_ingredients()
    is_valid = any(ing.lower() in ingredients.lower() for ing in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
