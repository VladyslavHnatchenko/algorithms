def bubble_sort(n_list):
    for pass_num in range(len(n_list)-1, 0, -1):
        for i in range(pass_num):
            if n_list[i] > n_list[i+1]:
                temp = n_list[i]
                n_list[i] = n_list[i+1]
                n_list[i+1] = temp


n_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubble_sort(n_list)
print(n_list)


# example
# def bubble_sort(array):
#     length_of_array = len(array) - 1
#
#     for i in range(length_of_array):
#         for j in range(length_of_array - i):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#     return array
#
#
# array = [2, 1, 5, 4, 3]
# print(bubble_sort(array))


# example
# def bubble_sort(A):
#     j = len(A) - 1
#     isNotOrdered = True
#     while isNotOrdered:
#         isNotOrdered = False
#         for i in range(0, j):
#             if A[i] > A[i+1]:
#                 A[i], A[i+1] = A[i+1], A[i]
#                 isNotOrdered = True
#
#         j -= 1

# example
# def bubble_sort(A):
#     for j in range(len(A) - 1):
#         for i in range(len(A) - 1 - j):
#             if A[i] > A[i+1]:
#                 A[i], A[i+1] = A[i+1], A[i]
#
# print(bubble_sort([4, 2]))
