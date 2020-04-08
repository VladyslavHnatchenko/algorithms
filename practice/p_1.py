# MERGE sort
def merge_sort(a_list):
    print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", a_list)


a_list = [54, 33, 4, 5, 1, 30, 12, 123, 44]
merge_sort(a_list)
print(a_list)

# SHELL sort
# def shell_sort(alist):
#     sublistcount = len(alist)//2
#     while sublistcount > 0:
#         for startposition in range(sublistcount):
#             gap_insertion_sort(alist, startposition, sublistcount)
#
#         print("After increments of size", sublistcount, "The list is", alist)
#         sublistcount = sublistcount // 2
#
#
# def gap_insertion_sort(alist, start, gap):
#     for i in range(start+gap, len(alist), gap):
#
#         currentvalue = alist[i]
#         position = i
#
#         while position >= gap and alist[position-gap] > currentvalue:
#             alist[position] = alist[position-gap]
#             position = position-gap
#
#         alist[position] = currentvalue
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(alist)
# print(alist)

# insertion sort
# def insertion_sort(a_list):
#     for index in range(1, len(a_list)):
#         current_value = a_list[index]
#         position = index
#
#         while position > 0 and a_list[position - 1] > current_value:
#             a_list[position] = a_list[position - 1]
#             position = position - 1
#         a_list[position] = current_value
#
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 30, 3]
# insertion_sort(a_list)
# print(a_list)

# selection sort
# def selection_sort(a_list):
#     for fill_slot in range(len(a_list)-1, 0, -1):
#         position_of_max = 0
#         for location in range(1, fill_slot + 1):
#             if a_list[location] > a_list[position_of_max]:
#                 position_of_max = location
#
#         temp = a_list[fill_slot]
#         a_list[fill_slot] = a_list[position_of_max]
#         a_list[position_of_max] = temp
#
#
# a_list = [33, 45, 2, 34, 5, 99, 45, 20]
# selection_sort(a_list)
# print(a_list)

# bubble sort
# def bubble_sort(a_list):
#     for pass_num in range(len(a_list)-1, 0, -1):
#         for i in range(pass_num):
#             if a_list[i] > a_list[i + 1]:
#                 temp = a_list[i]
#                 a_list[i] = a_list[i + 1]
#                 a_list[i + 1] = temp
#
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)

# binary search in list
# def binary_search(a_list, item):
#     first = 0
#     last = len(a_list) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if a_list[midpoint] == item:
#             found = True
#         else:
#             if item < a_list[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
#
# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(test_list, 3))
# print(binary_search(test_list, 13))
