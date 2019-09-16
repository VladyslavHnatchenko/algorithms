"""Find name of object"""


class A:
    pass


B = A
a = B()
b = a
print(b)
print(a)
print(B)
print(A)
