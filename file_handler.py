import json

from ciphers import caesar as CaesarCipher
from database import DbHandler as db


class FileManager:
    def __init__(self, db_handler: db):
        self.db = db_handler

    def encrypt_json_file(self, file_path: str, shift: int) -> None:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                encrypted_data_from_json = {}

                for key, value in data.items():
                    encrypted_text = CaesarCipher.encrypt(value, shift)
                    encrypted_data_from_json[key] = encrypted_text

                for key, encrypted_text in encrypted_data_from_json.items():
                    print("Key:", key, "Encrypted text:", encrypted_text)
                    self.db.add_to_ciphers(key, encrypted_text)
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    def decrypt_json_file(self, file_path: str, shift: int) -> None:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                decrypted_data_from_json = {}

                for key, value in data.items():
                    decrypted_text = CaesarCipher.decrypt(value, shift)
                    decrypted_data_from_json[key] = decrypted_text

                for key, decrypted_text in decrypted_data_from_json.items():
                    print("Key:", key, "Decrypted text:", decrypted_text)
                    self.db.add_to_ciphers(key, decrypted_text)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
