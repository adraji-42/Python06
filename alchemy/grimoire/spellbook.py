from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:

    return (
        f"{spell_name} (fire air - "
        f"{"VALID" if validate_ingredients(ingredients) else "INVALID"})"
    )
