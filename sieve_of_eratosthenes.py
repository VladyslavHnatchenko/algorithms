"""
In this example of the implementation of the Eratosthenes algorithm,
the list is filled with numbers from 0 to n inclusive, so that the indices
of the elements coincide with their values. Further, all complex numbers are
replaced by zeros:
"""
n = int(input())

# List with numbers 0 to n.
a = []
for i in range(n + 1):
    a.append(i)

# The second element is - 1, which is not considered simple hammer it
# from scratch.
a[1] = 0

# Starting since - 3.
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

# Turning the list into set, get rid of all zeros except one.
a = set(a)
a.remove(0)
print(a)
