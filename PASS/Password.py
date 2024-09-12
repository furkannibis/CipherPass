from os import path, remove, mkdir
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.pass_file_key = '.pass/.filekey.key'
        self.pass_file_path = '.pass/.pass.txt'
        
    def check_key_file(self):
        return path.exists(self.pass_file_key)
        
    def check_pass_file(self):
        return path.exists(self.pass_file_path)
    
    def get_key(self):
        if not self.check_key_file():
            raise FileNotFoundError("Key file not found.")
        with open(file=self.pass_file_key, mode='rb') as keyFile:
            return keyFile.read()
    
    def generate_key_file(self):
        key = Fernet.generate_key()
        with open(file=self.pass_file_key, mode='wb+') as filekey:
            filekey.write(key)
    
    def generate_pass_file(self):
        with open(file=self.pass_file_path, mode='w+', encoding='utf-8') as passFile:
            passFile.write("")
    
    def generate_file_dir(self):
        mkdir('.pass')
    
    def decrypt_pass_file(self) -> str:
        if not self.check_pass_file():
            raise FileNotFoundError("Password file not found.")
        
        with open(file=self.pass_file_path, mode='rb') as passFile:
            encrypted = passFile.read()

        encrypted_lines = encrypted.split(b'\n')
        fernet = Fernet(self.get_key())
        try:
            decrypted_lines = [fernet.decrypt(line).decode() for line in encrypted_lines if line]
        except Exception as e:
            raise RuntimeError("Failed to decrypt the file. The file might be corrupted or the key might be incorrect.") from e
        return decrypted_lines

    def add_pass_file(self, app: str, username: str, password: str):
        fernet = Fernet(self.get_key())
        new_line = f'{app} | {username} | {password}'
        encrypted = fernet.encrypt(new_line.encode())
        
        with open(file=self.pass_file_path, mode='ab') as passFile:
            passFile.write(encrypted + b'\n')

    def check_cipherpass(self, username: str, password: str) -> bool:
        decrypt = self.decrypt_pass_file()[0]
        user_entries = f'cipherpass | {username} | {password}'
        if decrypt == user_entries:
            return True
        else:
            return False
    
    def find_app_username(self, app: str) -> str:
        for inf in self.decrypt_pass_file():
            if app in inf:
                return inf.split(' | ')[1]
    
    def find_app_password(self, app: str) -> str:
        for inf in self.decrypt_pass_file():
            if app in inf:
                return inf.split(' | ')[2]