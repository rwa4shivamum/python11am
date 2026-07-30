# student1 = {
#     "name":"jkasd",
#     "age":21,
#     "isAdult":True,
#     "salary":23000.01
# }
# student2 = {}

# print(dir(student1))
# student2 = student1.copy()
# print(student1.fromkeys("name"))#we'll see later
# print(student1.get("name")) #it print the value of given key
# lst = student1.items()
# print(lst)
# print(student1.keys())
# print(student1.pop("name")) #return value and delete that particular key:value pair
# print(student1.popitem()) #this return the last key:value pair and also delete the last key:value pair
# print(student1.setdefault("age")) #this will go in depth
# print(student1.update(student2)) #this we'll goona revise
# print(student1,student2)



# lst = [
#     {
#     "name":"jkasd",
#     "age":21,
#     "isAdult":True,
#     "salary":23000.01
#    },
#    {
#     "name":"jkasd",
#     "age":21,
#     "isAdult":True,
#     "salary":23000.01
#    },
#    {
#     "name":"jkasd",
#     "age":21,
#     "isAdult":True,
#     "salary":23000.01
#   }
# ]

# add1 = 2
# add2 = 2.5
# finaladd = add1 + add2
# print(type(finaladd))

# num = "3" 
# num2 = "2"
# print(int(num) + int(num2))
# print()

# students = [
#     {"id": 101, "name": "Alice", "score": 85},
#     {"id": 102, "name": "Bob", "score": 78},
#     {"id": 103, "name": "Charlie", "score": 92}
# ]
# stud = {"id": 101, "name": "Alice", "score": 85}
# # print(stud["name"])
# for i in range(0,len(students)):
#     print(students[i]["score"])

key = ["id","name","email"]
value = [101,"bob","bib@gmail.com"]
print(dir(dict))
print(dir(list))

dictionaryOFkeyVaolue = {}
dictionaryOFkeyVaolue['id'] = 121
print(dictionaryOFkeyVaolue)
for i in range(0,len(key)):
    dictionaryOFkeyVaolue[f"{key[i]}"] = value[i]

print(dictionaryOFkeyVaolue)

# help(list)

lst = [1,2,3,4]
print(lst[::-1])#reverse   