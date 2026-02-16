def validate_ingredients(ingredients: str) -> str:

    valid = ["fire", "water", "earth", "air"]
    return (
        f"{ingredients} - VALID"
        if any(True if v in ingredients else False for v in valid)
        else f"{ingredients} - INVALID"
    )
