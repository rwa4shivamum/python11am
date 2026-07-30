"""___________________________SET__________________________________________
1.unordered: The elements in a set do not have a defined order, and you cannot access them using indexes.
2.unique ELement
4.mutable
4.dynamic size
"""
ste1  = {1,2,3,3,4,4}

ste2 = ste1.copy()
print(ste2)#{1, 2, 3, 4}
ste1.add(7)
print(ste1)#{1, 2, 3, 4, 7}
print(ste1.difference(ste2))
# ste1.difference_update(ste2)
#discard, isdisjoint,remove,union, update
# print(ste1.intersection(ste2))
# ste1.intersection_update(ste2)
#issubset
# print(ste1.issubset(ste2))
# print(ste1.issuperset(ste2))
print(ste1.symmetric_difference(ste2))
# ste1.symmetric_difference_update(ste2)
print(ste1)
print(ste1, ste2)
print(dir(ste1))


#st1 = {1,2,3,4,5,6,7,8,9}
#str2 = {1,2}
#str3 = {3,4}

"""
Student1:
name:"shivma"
age:22
rollNo:22
address:"jksfn"
parentDetail:"jkf"

student1={
  name:"hsiua",
  age:22,
  rollNo:
}
student1={
  name:"hsiua",
  age:22,
  rollNo:
}
student1={
  name:"hsiua",
  age:22,
  rollNo:
}
student1={
  name:"hsiua",
  age:22,
  rollNo:
}
student1={
  name:"hsiua",
  age:22,
  rollNo:
}
student1={
  name:"hsiua",
  age:22,
  rollNo:
}


studentName,RollNo, age, address, parentDetail
Shivam       22     22   "jksn"  "jsfd"     


name1="shivam"
age1=22
rollNo1=22

name2="iojsd"
"""