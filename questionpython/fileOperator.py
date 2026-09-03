list = ["apple mango orage", "mango", "orange"]
#delete6
find1 = "orage"
lst2 = []
for i in range(len(list)):
    if(list[i].find(find1) >= 0):
        print(list[i])

# print(lst2)
# str = "apple mango orage"
# print(str.find("o"))
# print(dir(str))

class BankAccount:
    def __add(self):
        return 2+3

    def display(self):
        return self.__add()

person1 = BankAccount()
print(person1.display())