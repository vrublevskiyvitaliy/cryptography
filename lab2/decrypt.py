# -*- coding: utf-8 -*-
import codecs


GROUP_LEN = 3


def decrypt():
    with codecs.open('encrypt.txt', 'r') as encrypt_file:
        total_line = ''.join(encrypt_file.readlines())

    key = get_key()
    decrypt_message = rearange_blocks(total_line, key)

    print(decrypt_message)

    with codecs.open('decrypt.txt', 'w') as decrypt_file:
        decrypt_file.write(decrypt_message)


def rearange_blocks(message, key):
    decrypted_message = [''] * len(key)
    index = 0
    for block in key:
        number = block - 1
        block_str = message[index * GROUP_LEN : (index + 1) * GROUP_LEN]
        decrypted_message[number] = block_str
        index += 1

    return ''.join(decrypted_message)


def get_key():
    with codecs.open('key.txt', 'r') as key_file:
        total_line = ''.join(key_file.readlines())
    key = total_line.split(' ')
    key = [int(element) for element in key]
    return key

decrypt()