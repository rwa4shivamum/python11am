# from functools import reduce
# expression = (5*3) + 5 + (5*3) 
# lst = [1,2,3,4,5,6]
# expression  = 3%10 + 3+5 + 5**2 + lst[2]
# result = 1 + 2 * 3 / 4 ** 2
# #            6   /   16
# print(6/16)
# print(result)  

# # Output: 
# # 1.375


# ##Map, filter, reduce, list comprehension
# lst = [1,2,3,4,5,6]
# lstSquare = list(map(lambda a: a*2, lst))
# filterOfEvenNum = list(filter(lambda a:a%2==0,lst)) #this filter out the even number
# filterOfEvenNumlstCompre = [i for i in lst if i%2==0]
# #reduce always return a single number or a single value
# reduceListinSingleValue = reduce(lambda result, curr: result * curr, lst, 10)
# print(reduceListinSingleValue)
# result = 10
# for i in lst:
#     result = result * i
# print(result)
# print(lstSquare, filterOfEvenNum, filterOfEvenNumlstCompre)



def pow(n, ex=2):
    return n**ex

print(pow(10))


def create_profile(name, age=18,city="Unknown"):
    print(f"name:{name},age={age}, city={city}")

create_profile("shivam",22, "mumbai")


def sum_all(*args):
    result = 0
    for i in args:
        result += i
    print(result)

sum_all(10,20,30,40)


def printInfo(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])

printInfo(name="shivam",age=22,grade='b+')  