"""Gave the number. Find the sum and product of its numbers."""

a = abs(int(input()))

summ = 0
mult = 1

while a > 0:
    digit = a % 10
    summ += digit
    mult *= digit
    a = a // 10


print("Sum:", summ)
print("Multiplication:", mult)
