from random import randint


# function implementation
def set_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


a = []
for i in range(10):
    a.append(randint(1, 99))

print(a)
set_sort(a)
print(a)


# 1.0 example
# N = 10
# arr = []
# for i in range(N):
#     arr.append(randint(1, 99))
#
# print(arr)
#
# i = 0
#
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if arr[j] < arr[m]:
#             m = j
#         j += 1
#
#     arr[i], arr[m] = arr[m], arr[i]
#     i += 1
#
# print(arr)
