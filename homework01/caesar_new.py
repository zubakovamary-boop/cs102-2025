def encrypt_poly_shift(plaintext: str, odd_shift: int, even_shift: int) -> str:
    ciphertext = ""
    alph_size = 32
    odd_shift %= alph_size
    even_shift %= alph_size
    for i, ch in enumerate(plaintext):
        position_in_str = i + 1
        if position_in_str % 2 == 1:
            shift = odd_shift
        else:
            shift = even_shift

        if "А" <= ch <= "Я":
            position = ord(ch) - ord("А")
            new_position = (position + shift) % alph_size
            new_ch = chr(ord("А") + new_position)
            ciphertext += new_ch
        elif "а" <= ch <= "я":
            position = ord(ch) - ord("а")
            new_position = (position + shift) % alph_size
            new_ch = chr(ord("а") + new_position)
            ciphertext += new_ch
        else:
            ciphertext += ch

    return ciphertext


print(encrypt_poly_shift("привет, пайтон", 1, 2))
