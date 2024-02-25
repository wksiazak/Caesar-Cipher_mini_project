class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord("z"):
                        shifted -= 26
                    encrypted_text += chr(shifted)
                elif char.isupper():
                    if shifted > ord("Z"):
                        shifted -= 26
                    encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, shift):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord("a"):
                        shifted += 26
                    decrypted_text += chr(shifted)
                elif char.isupper():
                    if shifted < ord("A"):
                        shifted += 26
                    decrypted_text += chr(shifted)
            else:
                decrypted_text += char
        return decrypted_text


class CaesarCipherFacade:
    def __init__(self):
        self.cipher = None
        self.shift = None

    def set_shift(self, shift):
        self.shift = shift
        self.cipher = CaesarCipher(shift)

    def encrypt_message(self, plaintext):
        return self.cipher.encrypt(plaintext, self.shift)

    def decrypt_message(self, ciphertext):
        return self.cipher.decrypt(ciphertext, self.shift)


if __name__ == "__main__":
    facade = CaesarCipherFacade()

    while True:
        print("Welcome in Ceasar cipher script, please select option: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            facade.set_shift(shift)
            encrypted_text = facade.encrypt_message(text)
            print("Encrypted:", encrypted_text)
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            facade.set_shift(shift)
            decrypted_text = facade.decrypt_message(text)
            print("Decrypted:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
