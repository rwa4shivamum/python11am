from datetime import datetime, date, time, timedelta
now = datetime.now()
dt2 = datetime.strptime("31-Aug-2026 11:00 AM", "%d-%b-%Y %I:%M %p")
print(dt2)
'''
module are three Types
1.inbuilt Module(when Python Got Installed it comes with that like, datatime, math, randome, uuid)
2.user defined module(when we create funciton if we wanna use that funciuton in another file then we export that function and use into another file we'll see this later )
3.Third Party Module(we install this type of module in local system by using python package manager and use it)
'''

import time
# print(time.time())
# time.sleep(2)
# print(time.ctime())  

# Measure time taken by code
start = time.time()
# def factorial(n):
#     if(n==1):
#         return 1
#     return n*factorial(n-1)

# print(factorial(800))
end = time.time()
print("Time taken:", end - start)
import math
# print(dir(math))
# print(math.ceil(4.16))
# print(math.floor(4.16))
# print(math.pi())
# print(math.factorial(5))
# print(math.pow())


import random

print(random.random()) #0to1
print(random.randint(1,100))

print(random.sample(range(1, 50), 6))


import uuid
#10000000-object-arrayof object-listofobject-> push this on db uuid moudle
#combination of this ipv4 192.168.0.1 -> 400cr -> world Population->800cr-> minimum 2 800*2=1600
#public ip private ipv6
print(uuid.uuid4())  
print(uuid.uuid1())     
u = uuid.uuid4()
print(str(u))  

from functools import reduce
#it convert an array into single digit number
lst = [1,2,3,4,5]
#15
result = 0
for i in range(len(lst)):
    result = result + lst[i]

print(result)#sum of all eleent in list