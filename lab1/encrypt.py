# -*- coding: utf-8 -*-
import lang
import random
import codecs


def encrypt():
    with codecs.open('origin.txt', 'r', 'utf-8') as origin_file:
        lines = origin_file.readlines()

    decrypt_file = codecs.open('encrypt.txt', 'w', 'utf-8')

    alphabet = lang.get_alphabet()

    key = random.randint(1, 31)
    print "key = " + str(key)

    for line in lines:
        new_line = ''
        for char in line:
            if char.upper() in alphabet:
                new_line += get_corresponded_char(char, key)
            else:
                new_line += char
        decrypt_file.write(new_line)


def get_corresponded_char(char, key):
    is_lower = char.islower()
    char = char.upper()

    alphabet = lang.get_alphabet()

    index = alphabet.index(char)
    new_index = (index + key) % len(alphabet)

    new_char = alphabet[new_index]
    if is_lower:
        new_char = new_char.lower()
    return new_char

encrypt()