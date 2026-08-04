#input, print, primitive Data type: non-collection Data type: int, float, bool, string, 
#collection data type: list,list comprehension , tuple, set, frozenset, dictionary, string 

# lstComprs = [i for i in range(1,10) if i%2==0]
# print(lstComprs)
# name = input("Enter a input")
# lst = [1,2,3,4]
# dict(lst)
# set(lst)
# list()
# str()
# #dictionary = {}

#Function 
'''
-- A resuable block of code

'''


# print("Hello")
# if True:
#     print("Hello")
# print("Hello")
# for i in range(1,10):
#     print("HEllo")

# function add(a,b):

# num1 = 18
# num2 = 20
# print(num1+num2)

# num1 = 20
# num3 = 40
# print(num1 + num3)

# def add(a,b):
#     return a+b

# for i in range(1,100):
#     print(add(i,i+10))

# DRY (Don't Reapeat Yourself)

'''
Types of Function:
1.Built In Functions
print()
input()
#more than 60 built in function
2.UDF(User Defined Function)


TNRN(Take Nothing Return nothing)
TSRS(Take something Return something)
TNRS(take Nothing return something)
TSRN(Take something Return Nothing)
'''

# #TSRS
# def add(a,b):
#     return a+b

# add(2,3)

# #TNRN
# def add():
#     print(2+3)

# add()

# #TNRS
# def add():
#     return 2+3

# add()

# #TSRN
# def add(a,b):
#     print(a+b)

# add()




'''
Types of functions Argument/parameter
1.Required Positional Argument
2. option Argument
  i.Arbitary Argument
  ii.keyword Argument
3.Default Argument
'''

def add(a,b): #parameter
    return a+b

add(10,11)#argument
# add(10)


# function
'''
def funcitonName(parameter):
     body
     return

functionName(arguments)

Tpyes of gunction UDF, built-in functions

Tpyes of argument/parameter
1.Required positional arguments
'''

# def subtract(a,b,c):
#     print(a,b,c)

# subtract(2,3,4)


#default argument = the Argument set as parameter, and it cannot required argument while calling the function, if we pass argument then default argument was override , and it set end as parameter
def fruits(arg1,arg2,fruit="Cherry"): #default argument
    print(arg1,arg2,fruit)


fruits("mango", "pineapple")


#2nd Option argument
#i.arbitary argument
# def fruits(*args):
#     print(len(args))

# fruits()
# fruits("mango")
# fruits("mango", "apple")


#ii.keywords argument
def keywrds(**kwargs):
    print(kwargs)

keywrds(animal="cat", age=1)

def mixedArgs(*args,fruits="cj",**kwrgs):
    print(args, fruits,kwrgs)

mixedArgs(1,2,3,name="sjiva")










































# #default argument has been passed as last parameter
# def get_fruits(n1, n2='Kivy'):
#     print(n1,n2)
    
# get_fruits("apple","cherry")
# get_fruits("apple")

# def arbutary_argu(*args):
#     print(args)

# arbutary_argu("hello", "I am shivam")
# arbutary_argu()
# arbutary_argu("hello")

# def keyword(**kwargs):
#     print(kwargs)

# keyword(cheese=50, tomato=2, olives=5)

# print(print.__doc__) #this was the __doc__ function which gives o/p as 


# def mixOfargs(*args, fruit="hello", fruit1, **kwargs):
#     print(args,fruit, kwargs)

# mixOfargs(1,2,3,name="sjhvam", suranme="mishra")


# summation = lambda _: "banana"

# print(summation('hello'))