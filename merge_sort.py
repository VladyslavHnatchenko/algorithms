"""Merge sort."""


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

"""Two sorted lists can be merged into one sorted list O(n)."""
# def merge(A, B):
#     Res = []
#     i = 0
#     j = 0
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             Res.append(A[i])
#             i += 1
#         else:
#             Res.append(B[j])
#             j += 1
#     Res += A[i:] + B[j:]
#     return Res
#
#
# first = [1, 3, 5, 7, 9]
# second = [2, 4, 6, 8, 9, 10]
#
# print(merge(second, first))
