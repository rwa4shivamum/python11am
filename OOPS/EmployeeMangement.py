class Employee:
    def __init__(self, name, empId, salary):
        self.name = name
        self.empId=empId
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        if(new_salary > 0):
            self.__salary = new_salary
        else:
            return "salary Must be greater than 0"

    def display_info(self):
        print(f"Name: {self.name} and EmployeeId: {self.empId} salary: {self.__salary}")

    def work(self):
        print(f"Name: {self.name} is Working....")

class Developer(Employee):
    def __init__(self,name, empId, salary, programming_language):
        super().__init__(name, empId, salary)
        self.programming_langauge = programming_language

    def work(self):
        print(f"{super().work()} on this Programming Language {self.programming_langauge}")

    def display_info(self):
        return super().display_info()