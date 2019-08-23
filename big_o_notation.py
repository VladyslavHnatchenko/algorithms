import matplotlib.pyplot as plt
import numpy as np

"""Space Complexity"""

# example


def return_squares(n):
    square_list = []
    for num in n:
        square_list.append(num * num)

    return square_list


nums = [2, 4, 6, 8, 10]
print(return_squares(nums))

"""Worst vs Best Case Complexity"""

# example
# def search_algo(num, items):
#     for item in items:
#         if item == num:
#             return True
#         else:
#             return False
#
#
# nums = [2, 4, 6, 8, 10]
#
# print(search_algo(2, nums))

"""Finding the Complexity of Complex Functions"""

# example
# def complex_algo(items):
#     for i in range(5):
#         print("Python is awesome")
#
#     for item in items:
#         print(item)
#
#     for item in items:
#         print(item)
#
#     print("Big O")
#     print("Big O")
#     print("Big O")
#
#
# complex_algo([4, 5, 6, 8])

"""Quadratic Complexity O(n^2)"""
# example
# def quadratic_algo(items):
#     for item in items:
#         for item2 in items:
#             print(item, ' ', item2)
#
#
# quadratic_algo([4, 5, 6, 8])

"""Linear Complexity O(n)"""

# x = [2, 4, 6, 8, 10, 12]
# y = [4, 8, 12, 16, 20, 24]
#
# plt.plot(x, y, 'b')
# plt.xlabel('Inputs')
# plt.ylabel('Steps')
# plt.title('Linear Complexity')
# plt.show()

# example
# def linear_algo(items):
#     for item in items:
#         print(item)
#
#     for item in items:
#         print(item)
#
#
# linear_algo([4, 5, 6, 8])

# example
# x = [2, 4, 6, 8, 10, 12]
# y = [2, 4, 6, 8, 10, 12]
#
# plt.plot(x, y, 'b')
# plt.xlabel('Inputs')
# plt.ylabel('Steps')
# plt.title('Linear Complexity')
# plt.show()

# example
# def linear_algo(items):
#     for item in items:
#         print(item)
#
#
# linear_algo([4, 5, 6, 8])


"""Constant Complexity O(C)"""

# x = [2, 4, 6, 8, 10, 12]
#
# y = [2, 2, 2, 2, 2, 2]
#
# plt.plot(x, y, 'b')
# plt.xlabel('Inputs')
# plt.ylabel('Steps')
# plt.title('Constant Complexity')
# plt.show()


# example
# def constant_algo(items):
#     result = items[0] * items[0]
#     print(result)
#
#
# constant_algo([4, 5, 6, 8])


"""Factorial"""
# factorial version 2.0
# def fact2(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact2(n-1)
#
#
# print(fact2(5))


# factorial version 1.0
# def fact(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product
#
#
# print(fact(5))
