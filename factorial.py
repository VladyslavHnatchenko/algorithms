"""factorial via math module"""
from math import factorial

print(factorial(5))
# print(factorial(15))
# print(factorial(51))

"""factorial via recursion"""


def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


print(factorial(6))
# print(factorial(15))
# print(factorial(52))

"""factorial via 'for' loop"""

# n = int(input())
# factorial = 1
#
# for i in range(2, n+1):
#     factorial *= i
#
# print(factorial)

"""factorial via 'while' loop"""

# n = int(input())
#
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)
