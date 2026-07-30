# str = "hello world world world"
# print(str.count("world"))
# print(str.split(" "))
# print("hello\nworld")

# name = "john"

# print(f"")


# string is immutable - depth


#Q1
sentence = "Machine Learning and AI are trending"
indexOfAi = sentence.find("AI")
str1 = sentence.replace("AI", "Aritificial Intelligence")
print(str1)
print("apple,banana,mango".split(","))
print("-".join(["python", "is", "awesome"]))

str1 = """
  Here is my name
"""

str2 = "Hello I an shivan ajkbnd World"

# lst = []
# for i in sentence:
#     words = ""
#     if(i!=" "):
#         # print(i)
#         words = words + i
#     else:
#         words = ""
#         print(words)
#         lst.append(words)

# print(lst)

# str = "World"
# print("Hello " + str)

str = "Data123#Science!"
strlst = list(str)
stralpha = ""
for i in strlst:
    if(i.isalpha()):
        stralpha += i

print(stralpha)