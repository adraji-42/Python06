"""Module for basic transmutations using absolute imports."""

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmutes lead to gold.

    Returns:
        str: Result of the transmutation.
    """
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Transmutes stone to a gem.

    Returns:
        str: Result of the transmutation.
    """
    return f"Stone transmuted to gem using {create_earth()}"
