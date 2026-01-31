# Caesar Cipher Tool

A lightweight, reusable Caesar cipher library for Python.

> ⚠️ **Security Notice**  
> This library is for educational purposes only. It is **not cryptographically secure** and should **not** be used for sensitive data.

## Installation

```bash
pip install caesar-cipher-tool
```

## Usage

```python
from cipher_tool import encrypt, decrypt

# Encrypt a message
ciphertext = encrypt("Hello, World!", shift=3)
print(ciphertext)  # Khoor, Zruog!

# Decrypt a message
plaintext = decrypt(ciphertext, shift=3)
print(plaintext)   # Hello, World!
```

## Features

- **Simple API**: Easy-to-use encrypt/decrypt functions
- **Configurable shift**: Support for any shift value (0-25)
- **Case preservation**: Maintains uppercase and lowercase letters
- **Non-alphabetic handling**: Preserves punctuation, spaces, and numbers
- **Lightweight**: Minimal dependencies
- **Extensible**: Clean architecture for adding other cipher methods

## API Reference

### `encrypt(text, shift)`

Encrypts plaintext using Caesar cipher.

**Parameters:**
- `text` (str): The plaintext to encrypt
- `shift` (int): Number of positions to shift (0-25)

**Returns:** Encrypted ciphertext (str)

### `decrypt(text, shift)`

Decrypts ciphertext using Caesar cipher.

**Parameters:**
- `text` (str): The ciphertext to decrypt
- `shift` (int): Number of positions to shift (0-25)

**Returns:** Decrypted plaintext (str)

## Examples

```python
# Basic usage
encrypt("Hello", 3)      # "Khoor"
decrypt("Khoor", 3)      # "Hello"

# Mixed case and punctuation
encrypt("Hello, World!", 13)  # "Uryyb, Jbeyq!"

# Numbers and symbols are preserved
encrypt("Test123!", 5)        # "Yjxy123!"
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.