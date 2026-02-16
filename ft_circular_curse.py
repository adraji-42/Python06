from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:

    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    spells = ["fire air", "dragon scales"]

    for spell in spells:
        print(
            f"validate_ingredients(\"{spell}\"): {validate_ingredients(spell)}"
        )

    print("\nTesting spell recording with validation:")
    spells = [("Fireball", "fire air"), ("Dark Magic", "shadow")]

    for name, spell in spells:
        print(
            f"record_spell{(name, spell)}: "
            f"Spell recorded: {record_spell(name, spell)}"
        )

    print("\nTesting late import technique:")
    print(
        f"record_spell{("Lightning", "air")}: "
        f"Spell recorded: {record_spell("Lightning", "air")}"
    )

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely")


if __name__ == "__main__":
    main()
