"""
Enumeration of divisors is an algorithm used to determine whether
a natural number is simple or is it complex, that is, composite.
"""
import math
from math import sqrt

# 2.0 example


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    limit = sqrt(n)
    i = 2

    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(3):
    num = int(input())
    print(is_prime(num))

# 1.0 example
# n = int(input())
#
# if n < 2:
#     print("The number must high than 1.")
#     quit()
# elif n == 2:
#     print("This's simple number.")
#     quit()
#
# i = 2
# limit = int(math.sqrt(n))
#
# while i <= limit:
#     if n % i == 0:
#         print("This's complex number.")
#         quit()
#     i += 1
#
# print("This's simple number.")
