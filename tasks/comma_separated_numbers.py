"""Python: Generate a list and tuple with comma-separated numbers"""

values = input("Input some comma separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List : ", list)
print("Tuple : ", tuple)
