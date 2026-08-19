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
    def __init__(self,bankHolderName,accoutNo, pin):
        self.bankHolderName = bankHolderName
        self.accoutNo = accoutNo
        self.__balance = 0
        self.__pin = pin
        self.__transaction_history = []

    def withDraw(self,pin,amount):
        if pin != self.__pin:
            print("Invalid Pin")

        if amount <= 0:
            print("Invalid withdrwal Amount")

        if amount > self.__balance:
            print("Insuffiecent Balance")
            return

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawn {amount}")
        print("Withdraw Successfully")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("INcorrect old PIN")
            return

        if len(str(new_pin)) != 4:
            print("PIN must be 4 digits")
            return

        self._pin = new_pin
        print("Pin changed Successfully")

    def get_transaction_history(self, pin):
        if pin != self.__pin:
            print("Invalid Pin")
            return
        return self.__transaction_history
    
    def deposit(self,amount):
        if amount <= 0:
            print("INvalid deposit amount")
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit {amount}")

    def displayInfo(self,pin):
        if pin == self.__pin:
            print(f"AccounheolderName:{self.bankHolderName} and AccounBalace {self.__balance}")

person1 = BankAccount("harsh",123456789)
person1.display_info(1234) 
person1.deposit(2000) 
print(person1.check_balance(1234)) 
person1.withdraw(1234, 500) 
print(person1.get_transaction_history(1234))
