"""Test script for demonstrating absolute and relative import pathways."""

from typing import Callable, List
import alchemy.transmutation.basic
import alchemy.transmutation.advanced
import alchemy.transmutation


def main() -> None:
    """Executes the pathway debate demonstration."""
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(
        "philosophers_stone(): "
        f"{alchemy.transmutation.advanced.philosophers_stone()}"
    )
    print(
        "elixir_of_life(): "
        f"{alchemy.transmutation.advanced.elixir_of_life()}\n"
    )

    print("Testing Package Access:")
    funcs: List[str] = ["lead_to_gold", "philosophers_stone"]
    for name in funcs:
        try:
            func: Callable[[], str] = getattr(alchemy.transmutation, name)
        except Exception as e:
            print(f"Unexpected Error: {e}\n")
        print(f"alchemy.transmutation.{name}(): {func()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
