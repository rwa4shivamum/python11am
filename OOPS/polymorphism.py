"""
Method overloading-steps
-----------------
   -Single Class
   -Multiple Mehods(not for python)
   -method name must be same, but parameter different
   -For python: Use Single method with Arbitary Argument(*args)
"""
class Vehicle:
    def truck(self,*args):
        if len(args) == 0:
            print(f"truck is empty")
        elif len(args) == 1:
            print(f"truck is loaded {args[0]}")
        else:
            print(f"truck is overloaded {[i for i in list(args)]} ")

truck1 = Vehicle()

truck1.truck()
truck1.truck(10)
truck1.truck(10,20,30)


# tupl = (1,2,3,4,5,6)
# [print(i) for i in list(tupl)]

class India:
    def wearing(self):
        print("Wearing Dhoti Kurta")

class Pak(India):
    def wearing(self):
        print("Wearing Pathani")

abdul = Pak()
abdul.wearing()

class India:
    def wearing(self):
        print("Wearing Dhoti Kurta")

class Pak(India):
    def wearing(self):
        aman = India() #extra object create
        aman.wearing()
        print("Wearing Pathani")

abdul = Pak() #{}
abdul.wearing()


class India:
    def wearing(self):
        print("Wearing Dhoti Kurta")

class Pak(India):
    def wearing(self):
        super().wearing()
        print("Wearing Pathani")

abdul = Pak() #{}
abdul.wearing()