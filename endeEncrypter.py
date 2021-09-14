'''
Name: EnDe
About: Password Manager with GUI
Project Link: https://github.com/santhoshsunthar/EnDe

'''

import hashlib
from Cryptodome.Cipher import AES

class ende(object):
    def __init__(self, key, text):
        self.key = key
        self.text = bytes(text, 'utf-8')

        self.hashed_key_salt = dict()

        self.user_key = bytes(key, "utf-8")
        self.user_salt = bytes(key[::-1], "utf-8")

        self.hash_type = "SHA256"

        self.createHash()
        self.createCipher()
        
    def createHash(self):
        self.hasher = hashlib.new(self.hash_type)
        self.hasher.update(self.user_key)

        self.hashed_key_salt["key"] = bytes(self.hasher.hexdigest()[:32], "utf-8")

        self.hasher = hashlib.new(self.hash_type)
        self.hasher.update(self.user_salt)

        self.hashed_key_salt["salt"] = bytes(self.hasher.hexdigest()[:16], "utf-8")

    def createCipher(self):
        self.cipher_object = AES.new(self.hashed_key_salt["key"], AES.MODE_CFB, self.hashed_key_salt["salt"])

        encrypted_content = self.cipher_object.encrypt(self.text)

        return encrypted_content