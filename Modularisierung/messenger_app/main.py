from formatter.plain import format_message as plain_format
from formatter.stylish import format_message as stylish_format


def main():
    text = input("Gib eine Testnachricht ein: ")

    print("\nWähle einen Formatierungsstil:")
    print("1) plain")
    print("2) stylish")
    choice = input("Deine Wahl (1/2): ").strip()

    if choice == "1":
        result = plain_format(text)
    elif choice == "2":
        result = stylish_format(text)
    else:
        print("Ungültige Auswahl – nutze plain als Standard.")
        result = plain_format(text)

    print("\n--- Ergebnis ---")
    print(result)


if __name__ == "__main__":
    main()