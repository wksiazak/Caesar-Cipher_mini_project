from Caesar_cipher_scrypt import *
from Caesar_cipher_scrypt import CaesarCipher, CaesarCipherFacade


class TestCaesarCipher:

    def test_encrypt_lowercase(self):
        cipher = CaesarCipher(3)
        assert cipher.encrypt("abc", 3) == "def"

    def test_encrypt_uppercase(self):
        cipher = CaesarCipher(5)
        assert cipher.encrypt("XYZ", 5) == "CDE"

    def test_encrypt_mixed_case(self):
        cipher = CaesarCipher(1)
        assert cipher.encrypt("AbC XyZ", 1) == "BcD YzA"

    def test_decrypt_lowercase(self):
        cipher = CaesarCipher(2)
        assert cipher.decrypt("cde", 2) == "abc"

    def test_decrypt_uppercase(self):
        cipher = CaesarCipher(4)
        assert cipher.decrypt("EFGH", 4) == "ABCD"

    def test_decrypt_mixed_case(self):
        cipher = CaesarCipher(1)
        assert cipher.decrypt("BcD YzA", 1) == "AbC XyZ"
