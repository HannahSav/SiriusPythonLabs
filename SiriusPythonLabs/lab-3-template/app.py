# Created by Hannah at 05.10.2023 0:21


import math


def normal_input(a):
    if isinstance(a, int) and a > 0:
        return True
    return False


def is_prime(a):
    if not normal_input(a):
        raise AssertionError
    a = abs(a)
    if a < 2:
        return False
    divider = 2
    while divider <= math.ceil(math.sqrt(a)):
        if divider != a and a % divider == 0:
            return False
        divider += 1
    return True


def next_prime(a):
    if not normal_input(a):
        raise AssertionError
    if a <= 1:
        return 2
    while not is_prime(a):
        a += 1
    return a


def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    gcd_meaning = 1
    a_fact = a
    b_fact = b
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0 and is_prime(i):
            while a_fact % i == 0 and b_fact % i == 0:
                gcd_meaning *= i
                a_fact //= i
                b_fact //= i
    return gcd_meaning


def are_coprime(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise AssertionError
    a = abs(a)
    b = abs(b)
    if gcd(a, b) == 1:
        return True
    return False


def best_prime_hard():
    number_start = 2
    while True:
        number_start = next_prime(number_start)
        print("Best prime number: {}".format(number_start))
        # print("len arr", len(prime_numbers_array))
        # for i in range(len(prime_numbers_array)):
        #    print(prime_numbers_array[i], end = ', ')
        number_start += 2  # because it should be odd