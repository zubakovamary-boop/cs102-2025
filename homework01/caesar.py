def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift = shift % 26
    for ch in plaintext:
        if "A" <= ch <= "Z":
            position = ord(ch) - ord("A")
            new_position = (position + shift) % 26
            new_ch = chr(ord("A") + new_position)
            ciphertext += new_ch
        elif "a" <= ch <= "z":
            position = ord(ch) - ord("a")
            new_position = (position + shift) % 26
            new_ch = chr(ord("a") + new_position)
            ciphertext += new_ch
        else:
            ciphertext += ch

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    shift = shift % 26
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            position = ord(ch) - ord("A")
            new_position = (position - shift) % 26
            new_ch = chr(ord("A") + new_position)
            plaintext += new_ch
        elif "a" <= ch <= "z":
            position = ord(ch) - ord("a")
            new_position = (position - shift) % 26
            new_ch = chr(ord("a") + new_position)
            plaintext += new_ch
        else:
            plaintext += ch
    return plaintext


a = encrypt_caesar("Python3.6", 3)
b = decrypt_caesar("Sbwkrq3.6", 3)
print(a, b)
