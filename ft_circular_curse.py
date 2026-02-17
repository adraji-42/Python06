from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:

    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    spells = ["fire air", "dragon scales"]

    for spell in spells:
        try:
            print(
                f"validate_ingredients(\"{spell}\"): "
                f"{validate_ingredients(spell)}"
            )
        except Exception as e:
            print(f"Unexpected Error: {e}\n")

    print("\nTesting spell recording with validation:")
    spells = [("Fireball", "fire air"), ("Dark Magic", "shadow")]

    for name, spell in spells:
        try:
            print(
                f"record_spell{(name, spell)}: "
                f"Spell recorded: {record_spell(name, spell)}"
            )
        except Exception as e:
            print(f"Unexpected Error: {e}\n")

    print("\nTesting late import technique:")
    print(
        f"record_spell{("Lightning", "air")}: "
        f"Spell recorded: {record_spell("Lightning", "air")}"
    )

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}\n")
