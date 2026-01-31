from cipher_tool.caesar.model import CaesarCipher

def encrypt(text: str, shift: int = 1) -> str:
    cipher = CaesarCipher(shift)
    result = ""

    for char in text:
        result += cipher._shift_char(char, cipher.shift)

    return result


if __name__ == "__main__":
    raise RuntimeError(
        "This module cannot be run directly. Import it instead."
    )