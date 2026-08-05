# fact = 1
# for i in range(5):
#     fact += fact * i

# print(fact)


# def factorial(n):


def add(a,b):

    print(a+b, "here from 13")
    print("a", "here from 14")
    return a+b

print(add(2,3), "here from 16")

# num = None


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))



#Anonymous / lambda function
'''
-- A function without a name is called anonymous function
-- This function does'nt have a multi-line body
-- This function must return some value or expression.

Syntax:
------
lambda arguments: expression

summation = lambda a, b: a+b
'''

summation = lambda a, b: a+b
print(summation(2,3))

lstofSquare = lambda lst:[i**2 for i in lst]
print(lstofSquare([1,2,3,4]))



#global keyword
name = "ksjfdn" #global scope 
def callname():
    global surname
    surname = "ksbdf" #function scope or local scope
    print(name)

print(surname)
callname()
# print()


#defn-reuable block of code
'''
Types of function
i.user define
ii.built-in funciton(almost 60+)

Types of argument/parameters
1.positional argument/parmeter
2.option argument
 i.arbitary type(tuple)
 ii.keyowrds type dectionary
3.default argument

property of default argument:
1.it always present as last argument
2.if we call function and the place where deafult argument lies then that argument will overide

optional argument
i.arbitary argument
  a.type was tuple
  b.funciton call with no argument, single argument, or multiple argument

ii.keywords
  a.type was dictionary
  b.funciton call with no argument, single argument, or multiple argument

mixed arguments

def mixdargs(*args, fruits="hello",**kwargs):
'''
