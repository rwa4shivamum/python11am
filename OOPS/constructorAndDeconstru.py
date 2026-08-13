# class Car:
#     def set_data(self,car, model, year):
#         self.car = car
#         self.model = model
#         self.year = year

#     def get_data(self):
#         print(f"Car {self.car} {self.model} {self.year}")


# car1 = Car()
# car1.set_data("Tata", "safari", 2021)
# car1.get_data()

# class Car:

#     def __init__(self,car, model, year):
#         self.car = car
#         self.model = model
#         self.__year = year
#         self.sterring = self.sterring

#     def get_data(self):
#             print(f"Car {self.car} {self.model} {self.year} {self.sterring}")

# car1 = Car("Tata", "safari", 2021)
# car1.get_data()



#default 

class BankAccount:
    def __init__(self,bankHolderName,accoutNo):
        self.bankHolderName = bankHolderName
        self.accoutNo = accoutNo
        self.__balance = 0
        self.__pin = 1234

    def withDraw(self,pin,amount):
        if pin == self.__pin and amount <= self.__balance:
            print("withdraw Succesfully")
            self.__balance = self.__balance - amount
        else:
            print("Invalid Pin OR Insufficient Amount")

    def deposit(self,amount):
        self.__balance += amount

    def displayInfo(self,pin):
        if pin == self.__pin:
            print(f"AccounheolderName:{self.bankHolderName} and AccounBalace {self.__balance}")

person1 = BankAccount("harsh",123456789)
person1.displayInfo(1234)
person1.deposit(2000)
person1.displayInfo(1234)
person1.withDraw(1234,2000)
person1.displayInfo(1234)

person1.__balance