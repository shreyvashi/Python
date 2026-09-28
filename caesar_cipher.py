def caesar(text, shift, encrypt=True):
    """Encrypt or decrypt text using the Caesar Cipher."""
    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 0 or shift > 25:
        return "Shift must be between 0 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def main():
    print("=== Caesar Cipher ===")
    text = input("Enter your message: ")

    try:
        shift = int(input("Enter shift value (0-25): "))
    except ValueError:
        print("Error: Shift must be an integer.")
        return

    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice in ("e", "encrypt"):
        result = encrypt(text, shift)
    elif choice in ("d", "decrypt"):
        result = decrypt(text, shift)
    else:
        print("Error: Invalid choice.")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()