import random

"""Functional style"""


def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]

        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quick_sort(L) + M + quick_sort(R)


print(quick_sort([3, 4, 1, 3, 4, 44, 5, 65, 6, 34]))

"""Quicksort Tony Hoare"""
# def quick_sort(A):
#     if len(A) <= 1:
#         return A
#     else:
#         q = random.choice(A)
#         L = []
#         M = []
#         R =[]
#         for elem in A:
#             if elem < q:
#                 L.append(elem)
#             elif elem > q:
#                 R.append(elem)
#             else:
#                 M.append(elem)
#         return quick_sort(L) + M + quick_sort(R)
#
#
# print(quick_sort([1, 12, 5, 3, 55, 109, 43, 12, 333, 8]))
