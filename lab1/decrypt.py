# -*- coding: utf-8 -*-
import lang
import codecs


def calculate_statistic():
    with codecs.open('encrypt.txt', 'r', 'utf-8') as origin_file:
        lines = origin_file.readlines()

    alphabet = lang.get_alphabet()

    statistic = [0] * len(alphabet)

    for line in lines:
        for char in line:
            if char.upper() in alphabet:
                index = alphabet.index(char.upper())
                statistic[index] += 1

    statistic_per_char = {}

    for index, value in enumerate(statistic):
        if statistic[index] > 0:
            statistic_per_char[alphabet[index]] = statistic[index]

    statistic_per_char = sorted(statistic_per_char.items(), key=lambda x: x[1], reverse=True)

    for key, value in statistic_per_char:
        print key, value
        #print valuevalue
        #print '=' * 20


def replace():
    with codecs.open('encrypt.txt', 'r', 'utf-8') as origin_file:
        line = ''.join(origin_file.readlines())

    my_dict = {
        u'ы': u'о',

        #u'ф': u'e',
        #u'ф': u'a',
        u'ф': u'и',
        #u'с': u'а',
        u'с': u'e',
        u'ю': u'т',
        u'щ': u'н',
        #u'м': u'и',
        u'м': u'а',
        u'я': u'у',
        u'ц': u'к',
        u'л': u'я',
        u'э': u'с',
        u'ш': u'м',
        u'р': u'д',
        u'б': u'х',
        u'а': u'ф',
        u'в': u'ц',
        u'ч': u'л',
        u'з': u'ь',
        u'ъ': u'р',
        u'ь': u'п',
        u'п': u'г',
    }

    # u_dict = {}
    # for key in my_dict:
    #     print key
    #     u_dict[unicode(key)] = unicode(my_dict[key])

    new_line = ''
    for c in line:
        if c.lower() in my_dict.keys():
            ch = my_dict[c.lower()]
            if c.isupper():
                ch = ch.upper()
            new_line += ch
        elif c == ' ':
            new_line += c
        else:
            new_line += '*'
            # c

    print new_line


def lang_statistic():
    s = lang.DISTRIBUTION
    statistic_per_char = sorted(s.items(), key=lambda x: x[1], reverse=True)
    for key, value in statistic_per_char:
        print key, value

#calculate_statistic()
replace()