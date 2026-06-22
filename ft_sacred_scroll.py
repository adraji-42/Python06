"""Unified smart test script for the Sacred Scroll Mastery."""

import alchemy
import alchemy.elements as elements


def main() -> None:
    """Execution point using unified getattr logic."""
    print("\n=== Sacred Scroll Mastery ===\n")

    spell_names = [
        "create_fire", "create_water", "create_earth", "create_air"
    ]

    print("Testing direct module access:")
    for name in spell_names:
        try:
            print(f"alchemy.elements.{name}(): {getattr(elements, name)()}")
        except AttributeError:
            print(f"alchemy.elements.{name}(): AttributeError - not found")
        except Exception as e:
            print(f"Unexpected Error: {e}\n")

    print("\nTesting package-level access (controlled by __init__.py):")
    for name in spell_names:
        try:
            print(f"alchemy.{name}(): {getattr(alchemy, name)()}")
        except AttributeError:
            print(f"alchemy.{name}(): AttributeError - not exposed")
        except Exception as e:
            print(f"Unexpected Error: {e}\n")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}\n")
