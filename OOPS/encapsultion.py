class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.roll_no = int(input("ENter your rollNo"))
        self.__marks = 0
        self.__attendance = 0
        self.__grade = None

    def set_marks(self, marks):

        if marks < 0 or marks > 100:
            print("Marks must be between 0 to 100")
        else:
            self.__marks  = marks
            print("marks updated successfully")

    def get_marks(self):
        return self.__marks

    def set_attendance(self, attendance):
        if attendance < 0 or attendance > 100:
            print("Attendance must be between 0 to 100")
        else:
            self.__attendance = attendance
            print("Attendance Updated successfully")

    def get_attendance(self):
        return self.__attendance

    def calculate_grade(self):
        if self.__marks >= 90:
            self.__grade = "A+"
            print("Grade A+")
        elif self.__marks >= 80:
            self.__grade = "A"
            print("Grade A")
        elif self.__marks >= 70:
            self.__grade = "B+"
            print("Grade B+")
        elif self.__marks >= 60:
            self.__grade = "B"
            print("Grade B")
        elif self.__marks >= 50:
            self.__grade = "C"
            print("Grade C")
        elif self.__marks >= 40:
            self.__grade = "D"
            print("Grade D")
        else:
            self.__grade = "F"
            print("Fail")

    def is_passed(self):
        if self.__grade == "F":
            print("Student is Failed")
        else:
            print("Student Pass")

    def student_info(self):
        print("Name:", self.name) 
        print("Roll Number:", self.roll_no) 
        print("Marks:", self.__marks) 
        print("Attendance:", self.__attendance) 
        print("Grade:", self.__grade)


# student1 = Student()
# student1.set_marks()

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

person1 = BankAccount("harsh",123456789,1234)
person1.displayInfo(1234) 
person1.deposit(2000) 
person1.displayInfo(1234)
person1.withDraw(1234, 500) 
print(person1.get_transaction_history(1234))
person1.displayInfo(1234)
