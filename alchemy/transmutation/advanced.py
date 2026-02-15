"""Module for advanced transmutations using relative imports."""

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Creates the philosopher's stone.

    Returns:
        str: Result of the creation.
    """
    res_gold: str = lead_to_gold()
    res_heal: str = healing_potion()
    return f"Philosopher's stone created using {res_gold} and {res_heal}"


def elixir_of_life() -> str:
    """Creates the elixir of life.

    Returns:
        str: Success message.
    """
    return "Elixir of life: eternal youth achieved!"
