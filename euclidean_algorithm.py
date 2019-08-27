"""Euclidean Algorithm - finding the largest common divisor."""

# 2.0 example
a = 50
b = 129

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)


# 1.0 example
# a = 50
# b = 130
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(a+b)
