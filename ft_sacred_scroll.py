"""Unified smart test script for the Sacred Scroll Mastery."""

import alchemy
import alchemy.elements as elements
from typing import List, Callable


def main() -> None:
    """Execution point using unified getattr logic."""
    print("\n=== Sacred Scroll Mastery ===\n")

    spell_names: List[str] = [
        "create_fire", "create_water", "create_earth", "create_air"
    ]

    print("Testing direct module access:")
    for name in spell_names:
        try:
            spell_func: Callable[[], str] = getattr(elements, name)
            print(f"alchemy.elements.{name}(): {spell_func()}")
        except AttributeError:
            print(f"alchemy.elements.{name}(): AttributeError - not found")

    print("\nTesting package-level access (controlled by __init__.py):")
    for name in spell_names:
        try:
            package_func: Callable[[], str] = getattr(alchemy, name)
            print(f"alchemy.{name}(): {package_func()}")
        except AttributeError:
            print(f"alchemy.{name}(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
