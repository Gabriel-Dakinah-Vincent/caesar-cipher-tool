from cipher_tool.core.base import BaseCipher

class CaesarCipher(BaseCipher):
    def __init__(self, shift: int = 1):
        if not isinstance(shift, int):
            raise TypeError("Shift must be an integer")
        self.shift = shift % 26