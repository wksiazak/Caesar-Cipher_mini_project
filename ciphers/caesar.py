ALPHABET_SIZE = 26


def encrypt(text: str, shift: int) -> str:
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord("z"):
                    shifted -= ALPHABET_SIZE
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= ALPHABET_SIZE
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text: str, shift: int) -> str:
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord("a"):
                    shifted += ALPHABET_SIZE
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += ALPHABET_SIZE
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text
