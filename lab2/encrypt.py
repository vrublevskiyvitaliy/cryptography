# -*- coding: utf-8 -*-
import codecs
import permutation


GROUP_LEN = 3


def encrypt():
    with codecs.open('origin.txt', 'r') as origin_file:
        total_line = ''.join(origin_file.readlines())

    n = len(total_line) / GROUP_LEN
    key = permutation.generate_key(n)
    encrypt_message = rearange_blocks(total_line, key)

    with codecs.open('encrypt.txt', 'w') as encrypt_file:
        encrypt_file.write(encrypt_message)


def rearange_blocks(message, key):
    crypted_message = []
    for block in key:
        number = block - 1
        block_str = message[number * GROUP_LEN : (number + 1) * GROUP_LEN]
        crypted_message.append(block_str)

    return ''.join(crypted_message)

encrypt()