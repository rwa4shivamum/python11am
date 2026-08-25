#operator overloading
# class person:
#     def addTwoNumber(self,other):
#         self.number = 2
#         return self.number + other

# p1 = person()
# print(p1.addTwoNumber(3))
# class Box:
#     def __init__(self, volume):
#         self.volume = volume

#     def __add__(self, other):  # Overloading `+` operator
#         return Box(self.volume + other.volume)

# b1 = Box(10)
# b2 = Box(20)
# b3 = b1 + b2  # Calls __add__()

# print(b3.volume)  # Output: 30
#dunder methods
#abstraction using abstract class
#Abtstration:hide the logic car=

'''
 Import ABC module
 create a separte hiding logic class
 used inheritance to access the methods of the abstract class
 (Warning: don't create an instance of that abstract class)
'''

from abc import ABC, abstractmethod

#Abstract class
class Vehicle(ABC):
    def __init__(self):
        print("Here in constructor")

    @abstractmethod
    def start(self):
        print("Here I am this thing")

class Car(Vehicle):
    def start(self):
        super().start()
        return

car1 = Car()
car1.start()

