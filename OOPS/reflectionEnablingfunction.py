
class Car: #what we call this ?
    pass

car1 = Car() #instance
car2 = Car() #instance

class Animal:
    pass

dog = Animal()
print(isinstance(car1, Car))
print(isinstance(dog, Animal))

#isinstance i used to check whether that object belongs to which class


##############isSubclass()####################
class Animal():
    pass

class dog(Animal):
    pass

print(issubclass(dog, Animal))
print(issubclass(Animal, dog))
#this gonna used in inheritance widely


class Car:
    def start(self):
        pass

car1 = Car()
print(dir(car1))  # Output: List of attributes & methods

# print(dir(list))
# print(help(list))

class Car:
    def __init__(self):
        self.color = "Red"

car1 = Car()
print(hasattr(car1,"color"))
print(getattr(car1, "color"))
print(setattr(car1,"color", "yellow"))
print(getattr(car1,"color"))

class Car: #what we call this ?
    def __init__(self):
        self.color = "red"

car3 = Car()

class Animal:
    def __init__(self):
        self.animal = "Lion"

animal = Animal()
animal.__init__()
print(callable(__init__()))