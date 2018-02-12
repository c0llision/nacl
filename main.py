#!/usr/bin/env python3
import nacl.secret
import nacl.utils
from base64 import b64encode, b64decode


def encrypt(key, cleartext):
    box = nacl.secret.SecretBox(key)
    ciphertext = box.encrypt(cleartext)
    return b64encode(ciphertext)


def decrypt(key, data):
    box = nacl.secret.SecretBox(key)
    ciphertext = b64decode(data)
    cleartext = box.decrypt(ciphertext)
    return cleartext


def main():
    msg = b'test'
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    ciphertext = encrypt(key, msg)
    print(ciphertext)
    cleartext = decrypt(key, ciphertext)
    print(cleartext)


main()
