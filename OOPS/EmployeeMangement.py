class Employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,newamt):
        if newamt>0:
            self.__salary = newamt  
            print("salary undated")
        else:
            print("invalid salary")
    def display_info(self):
        print(f"""
        Name : {self.name}
        Employee id : {self.employee_id}
        Salary : {self.__salary}""")
    def work(self):
        print(f"{self.name} is working...")

class Developer(Employee):
    def __init__(self,name, employee_id, salary, programming_language):
        super().__init__(name,employee_id,salary)
        self.programming_language = programming_language
    def work(self):
        print(f"{self.name} on {self.programming_language} programming language")
    def display_info(self):
        super().display_info()
        print(f"          programming language : {self.programming_language}")  
    
class Manager(Employee):
    def __init__(self,name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    def work(self):
        print(f"the manager is managing team with {self.team_size} employee")
    def display_info(self):
        super().display_info()
        print(f"          team size : {self.team_size}") 

class Trainer:
    def __init__(self,expertise):
        self.expertise=expertise
    def conduct_training():
        print(f"conducting training on {expertise}")
    def work(self):
        print("gives training")

class SeniorDeveloper(Developer, Trainer):
    def __init__(self,name, employee_id, salary, programming_language, expertise, years_of_experience):
        Developer.__init__(self, name, employee_id, salary, programming_language)
        Trainer.__init__(self, expertise)
        self.years_of_experience = years_of_experience
    def work(self):
        print("software architecting + developer and program mentoring + training")
    def display_info(self):
        super().display_info()
        print(f"           years_of_experience: {self.years_of_experience}") 
        print(f"           expertise: {self.expertise}")


if __name__ == "__main__":
    emp = Employee("Bahubali", 101, 50000)
    dev = Developer("Nihar", 123, 70000, "Python")
    mgr = Manager("Devsena", 103, 90000, 10)
    senior = SeniorDeveloper("Diana", 104, 120000, "Python", "System Architecture", 8)
    employees = [emp, dev, mgr, senior]

    for i in employees:
        i.display_info()
        i.work()

    print(SeniorDeveloper.mro())
    print("MRO for SeniorDeveloper:")
    for cls in SeniorDeveloper.mro():
        print(cls.__name__)