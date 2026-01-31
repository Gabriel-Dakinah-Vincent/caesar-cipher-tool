class BaseCipher:
    def _shift_char(self, char: str, shift: int) -> str:
        if not char.isalpha():
            return char

        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)