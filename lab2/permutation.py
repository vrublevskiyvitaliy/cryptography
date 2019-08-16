import math
import random


def get_permutation(n, k):
    numbers = range(1, n+1)
    permutation = []
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, math.factorial(n))
        permutation.append(numbers[index])
        # remove handled number
        numbers.remove(numbers[index])

    return permutation


def get_random_permutation(n):
    fact_n = math.factorial(n)
    key = random.randint(1, fact_n)

    return get_permutation(n, key)


def generate_key(n):
    key = get_random_permutation(n)
    key_file = open('key.txt', 'w')

    key_string_array = [str(element) for element in key]
    key_string = ' '.join(key_string_array)
    key_file.write(key_string)

    key_file.close()
    return key