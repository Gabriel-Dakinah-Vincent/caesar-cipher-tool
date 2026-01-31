import pytest
from cipher_tool import encrypt, decrypt


def test_basic_encryption():
    """Test basic encryption functionality."""
    assert encrypt("ABC", 3) == "DEF"
    assert encrypt("xyz", 3) == "abc"


def test_basic_decryption():
    """Test basic decryption functionality."""
    assert decrypt("DEF", 3) == "ABC"
    assert decrypt("abc", 3) == "xyz"


def test_encrypt_decrypt_roundtrip():
    """Test that encrypt->decrypt returns original text."""
    message = "Hello, World!"
    shift = 3
    ciphertext = encrypt(message, shift)
    plaintext = decrypt(ciphertext, shift)
    assert plaintext == message


def test_case_preservation():
    """Test that case is preserved."""
    assert encrypt("Hello", 3) == "Khoor"
    assert encrypt("WORLD", 3) == "ZRUOG"


def test_non_alphabetic_preservation():
    """Test that non-alphabetic characters are preserved."""
    assert encrypt("Hello, World! 123", 3) == "Khoor, Zruog! 123"
    assert encrypt("Test@#$%", 5) == "Yjxy@#$%"


def test_different_shifts():
    """Test various shift values."""
    text = "Hello"
    assert encrypt(text, 0) == "Hello"
    assert encrypt(text, 1) == "Ifmmp"
    assert encrypt(text, 25) == "Gdkkn"


def test_wrap_around():
    """Test alphabet wrap-around."""
    assert encrypt("xyz", 3) == "abc"
    assert encrypt("XYZ", 3) == "ABC"
    assert decrypt("abc", 3) == "xyz"
    assert decrypt("ABC", 3) == "XYZ"


def test_empty_string():
    """Test empty string handling."""
    assert encrypt("", 3) == ""
    assert decrypt("", 3) == ""


@pytest.mark.parametrize("shift", [0, 1, 13, 25])
def test_multiple_shifts(shift):
    """Test multiple shift values with parametrized testing."""
    message = "The quick brown fox jumps over the lazy dog"
    ciphertext = encrypt(message, shift)
    plaintext = decrypt(ciphertext, shift)
    assert plaintext == message