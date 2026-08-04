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



