def record_spell(spell_name: str, ingredients: str) -> str:
    """Records a spell after validation using late import.

    Args:
        spell_name: Name of the spell.
        ingredients: Ingredients to validate.

    Returns:
        str: Success or failure message.
    """
    from .validator import validate_ingredients
    result: str = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
