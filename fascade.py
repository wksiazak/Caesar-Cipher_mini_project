from ciphers import caesar as CaesarCipher
from database import DbHandler
from file_handler import FileManager

MENU = """
    Welcome in Ceasar cipher script, please select option:
    1. Encrypt
    2. Decrypt
    3. Encrypt from json file
    4. Decrypt from json file
    5. Export ciphers from memory to file
    6. Exit
    """

DEFAULT_FILE_PATH = "data_to_encrypt.json"

DB_PATH = "caesar_collection_database.db"


class Manager:
    def __init__(self):
        self.db = DbHandler(DB_PATH)
        self.choices = {
            "1": self.encrypt_sentence,
            "2": self.decrypt_sentence,
            "3": self.encrypt_json,
            "4": self.decrypt_json,
            "5": self.export_to_file,
            "6": self.quit,
        }
        self.__is_running = True
        self.loop()

    def loop(self):
        self.db.create_table()
        while self.__is_running:
            print(MENU)
            user_choice = input("Choose an option: ")
            try:
                self.choices.get(user_choice, self.show_error)()
            except Exception as e:
                print(f"Program met an error - {e.args}")

    def encrypt_sentence(self):
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = CaesarCipher.encrypt(text, shift)
        self.db.add_to_ciphers(text, encrypted_text)
        print("Encrypted:", encrypted_text)

    def decrypt_sentence(self):
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = CaesarCipher.decrypt(text, shift)
        self.db.add_to_ciphers(text, decrypted_text)
        print("Decrypted:", decrypted_text)

    def encrypt_json(self):
        file_path = "data_to_encrypt.json"
        shift = 3
        FileManager.encrypt_json_file(self, file_path, shift)

    def decrypt_json(self):
        file_path = "data_to_decrypt.json"
        shift = 3
        FileManager.decrypt_json_file(self, file_path, shift)

    def export_to_file(self):
        self.db.export_all_ciphers("Ciphers", "results.txt")

    def show_error(self):
        print("Invalid choice. Please enter a valid option.")

    def quit(self):
        print("\nHave a nice day!")
        self.__is_running = False
