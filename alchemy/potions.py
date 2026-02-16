from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Brews a healing potion.

    Returns:
        str: The brewing result.
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Brews a strength potion.

    Returns:
        str: The brewing result.
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Brews an invisibility potion.

    Returns:
        str: The brewing result.
    """
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    """Brews a wisdom potion.

    Returns:
        str: The brewing result.
    """
    res: str = (
        f"{create_fire()}, {create_water()}, "
        f"{create_earth()} and {create_air()}"
    )
    return f"Wisdom potion brewed with all elements: {res}"
