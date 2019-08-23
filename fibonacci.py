"""fibonacci via recursion"""


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(1))
print(fibonacci(10))
print(fibonacci(33))

"""fibonacci via 'for' loop"""

# fib1 = fib2 = 1
# n = int(input())
#
# if n < 2:
#     quit()
#
# print(fib1, end=' ')
# print(fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
#
# print()

"""fibonacci via 'while' loop"""

# 2.0 example
# fib1 = fib2 = 1
#
# n = int(input("The number of Fibonacci element: ")) - 2
#
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
#
# print(fib2)

# 1.0 example
# Number = int(input("\nPlease Enter the Range Number: "))
#
# i = 0
# First_Value = 0
# Second_Value = 1
#
# # Find & Displaying Fibonacci series
# while i < Number:
#     if i <= 1:
#         Next = i
#     else:
#         Next = First_Value + Second_Value
#         First_Value = Second_Value
#         Second_Value = Next
#     print(Next)
#     i = i + 1
