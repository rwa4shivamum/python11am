'''
1.user Enter "abc"
2.user enter Zero or NEgative amount
3.User Enter more than bankBalance amount
'''

#logic of counNumber
def countDigits(digit):
    count = 0
    print(digit)
    while(digit > 0):
        print("here I am", digit)
        digit = digit // 10
        count = count + 1
    return count


class BankAccount:
    def __init__(self,name, AcoountNumber, balance):
        try:
            if  name.isdigit():
                raise ValueError("Enter a name")
            if countDigits(AcoountNumber) == 12:
                raise ValueError("Enter min 12 Digit")
            if balance.isdigit() and countDigits(balance) == 8:
                raise ValueError("Enter less then 10 Cr")
            self.name = name
            self.__AcoountNumber = AcoountNumber
            self.__balance = balance
        except (ValueError) as e:
            print("contructor in BankAccount ",e)
        else:
            print("Account Created Successfully")
        finally:
            print("Thank you to being with us.....")

    def withdraw(self,AcoountNumber, withdrawAmount):
        try:
            if countDigits(AcoountNumber) == 12 and self.__AcoountNumber != AcoountNumber:
                    raise ValueError("Enter min 12 Digit or Enter Account Number is Wrong")
            pass
        except:
            pass
        else:
            pass
        finally:
            pass


bankHolder1 = BankAccount(input("Enter a name"))

# name = "213"

# # help(str)
# # print(dir(str))
# print(name.isdigit() == True)
