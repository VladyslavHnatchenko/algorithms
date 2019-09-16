"""Calculate the sum of three given numbers, if the values are equal then
return thrice of their sum"""


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(2, 3, 4))
print(sum_thrice(4, 4, 4))
