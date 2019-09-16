"""Python: Count the number 4 in a given list"""


def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count


print(list_count_4([1, 4, 5, 55, 4]))
print(list_count_4([4, 4, 4, 4, 55, 6, 7]))
