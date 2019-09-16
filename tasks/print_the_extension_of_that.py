"""Python: Input a filename and print the extension of that"""

file_name = input("Input the file name: ")
f_extns = file_name.split(".")
print("The extension of the file is: " + repr(f_extns[-1]))

