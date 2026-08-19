# class Father:
#     def __init__(self):
#         self.surname = "patel"

#     def skinTone(self):
#         print("fair")

# class Mother:
#     def __init__(self):
#         self.motherName = "Rekha"

#     def nature(self):
#         print("Calm Nature")

# class Child(Father, Mother):
#     pass

# child1 =  Child()
# child1.skinTone()
# child1.nature()
# # print(child1.surname, child1.motherName)
# print(child1.motherName)
# print(issubclass(Child, Father))
# print(issubclass(Child, Mother))


#MRO Method Resolution order
#base 
class Father:
    # def __init__(self):
    #     print("Hello from Father")

    def skinTone(self):
        print("fair")

class Mother:
    def __init__(self):
        print("Hello from Mother")

    def nature(self):
        print("Calm Nature")

#derived class
class Child(Father, Mother):
    pass
    # def __init__(self):
    #     print("Hello from Child")



child1 = Child() #

print(Child.mro()) #here we call as Class

















#MRO stands for Method Resolution Order.




























# ============================================================
# TYPES OF INHERITANCE
# ============================================================

# 1. Single Inheritance
#    - One child class inherits from only one parent class.
#    - Simplest form of inheritance.
#    - Child gets all properties and methods of that single parent.

# 2. Multiple Inheritance
#    - One child class inherits from two or more parent classes.
#    - Child can use features of all its parents.
#    - Can create ambiguity (diamond problem) which is handled by MRO.

# 3. Multilevel Inheritance
#    - Inheritance happens in a chain (levels).
#    - Example: Grandparent → Parent → Child
#    - Child inherits from Parent, and Parent inherits from Grandparent.
#    - Features flow from top level to bottom level.
class GrandParent:
    def usedElectronic(self):
        print("Radio")

class Parent (GrandParent): #inherit properties from grandparent
    def usedElec(self):
        print("Television")

class Child (Parent): #inherir properties from parent as well grandparent
    def usedElec1(self):
        print("MObile Phones")

chil1 = Child()
chil1.usedElectronic()
chil1.usedElec()
chil1.usedElec1()

# 4. Hierarchical Inheritance
#    - One parent class has multiple child classes.
#    - All children inherit from the same parent.
#    - Useful when many classes share common features of one base class.

class parent1:
    def print1(self):
        print("Hello from parent 1")

class child1(parent1):
    pass

class child2(parent1):
    pass

child12 = child1()

child212 = child2()

child12.print1()
child212.print1()

# 5. Hybrid Inheritance
#    - Combination of two or more types of inheritance.
#    - Example: mixture of multiple + multilevel, or hierarchical + multiple, etc.
#    - Most complex form; requires careful design and understanding of MRO.
