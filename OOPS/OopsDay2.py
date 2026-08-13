#1️⃣ Simple Class with Empty Attributes (Initially None)
class Car:
    brand = None
    model = None
    year = None


car1 = Car() #object Creation Phase
print(car1.brand, car1.model, car1.year) #None

#2️⃣ Class with Predefined (Fixed) Values
class Car:
    brand = "Toyota"
    model = "Corolla"
    year = 2022

# Creating an object
car1 = Car()
car2 = Car()
print(car1.brand, car1.model, car1.year) 
# Printing values
print(car1.brand, car1.model, car1.year)  # Output: Toyota Corolla 2022

#3️⃣ Assigning Values After Object Creation
class Car:
    brand = None
    model = None
    year = None


car1 = Car() #object Creation Phase
print(car1.brand, car1.model, car1.year) #None
#phase value assign to abject
car1.brand = "Tata"
car1.model = "Safari"
car1.year = 2021
print(car1.brand, car1.model, car1.year)
# print(car1.)


#OOP 1st Pillar :- Encapsulation
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__year = 2021   #private attribute

    def get_manufaterYear(self):
        self.__year = 2024
        print(self.__year)

    def set_brand(self, brand):  # Setter
        self.brand = brand

    def get_brand(self):  # Getter
        return self.brand

car1 = Car("Tata", "safari")#instanse of class OR object
# car2 = Car("")
print(car1.model)
#print(car1.__year)#we cannot direct access the varible outside the class
car1.get_manufaterYear()

class Example:
    value = 100  # Class-level attribute

    def show(self):
        print(self.value)

obj1 = Example()
obj2 = Example()
obj1.show()  # Output: 100
obj2.show()  # Output: 100