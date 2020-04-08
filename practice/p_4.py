class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

# class Car:
#     car_count = 0
#     message1 = "Car start"
#
#     def __init__(self):
#         print("Start engine")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999
#
#     def __str__(self):
#         return "Car class Object"
#
#     def start(self):
#         message = "Start engine"
#         # self.name = name
#         # self.make = make
#         # self.model = model
#         return message
#
#     @staticmethod
#     def get_class_details():
#         print("This is class - Car")
#
#     # def stop(self):
#     #     print("Switch off engine")
#
#
# class Square:
#
#     @staticmethod
#     def get_squares(a, b):
#         return a*a, b*b
#
