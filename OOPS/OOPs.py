# OOPS stands for Object Oriented Programming
'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which contain both data (attributes) and behavior (methods). It allows for modular, reusable, and scalable code.

programming paradigm :- is the way to write the code.
  i.OOPS based programming paradigm
  ii.Function based or procedural programming paradigm (UDF->user defined funciton)

Data (attributes):- (just like varible in python or any language)
 i.name = "Sjhiva"

behavior (methods):- (just like functions we declare in python)

Pre-Requirement: Class & Object

Class:
- A bluePrint Of an Object (bluePrint:- e.g. Building floor blueprint before orginal sturture )

Object:
- A Instance of Class ( Based on BluePrint : building get constructed )
'''

class Car:
    _Company = None
    _model = None
    _color = None
    _year = None

    def setData(self, cm, ml, cl, yr):
        self._Company = cm
        self._model = ml
        self._color = cl
        self._year = yr

    
    def getData(self):
        print(f"This is company Name {self._Company} and model {self._model} and color {self._color} and year {self._year}")

car1 = Car()

car1.setData("Tata", "Nano", "peella", 2008)
# car1 = {
#      Company : None
#      model : None
#      color : None
#      year : None
#      setData():
#              self._Company = cm
#              self._model = ml
#              self._color = cl
#              self._year = yr
    
# }


car2 = Car()
car2.setData("BmW", "M4", "blue", 2023)

car1.getData()
car2.getData()



#Contructor

'''
studn ={
    namw
    age

    isleep()
    isEat()
    
}
'''

class Car:
    brand = None
    model = None
    year = None


car1 = Car()
print(car1.brand)