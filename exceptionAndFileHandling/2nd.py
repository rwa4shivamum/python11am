#built-in Function
#file
#file related operation
#file.close()
# with open("./response.jpeg", "rb") as source:
#     data = source.read()

# with open("photo_copy.jpg", "wb") as destination:
#     destination.write(data)

# Writing to a file
file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Age: 21\n")
file.write("Course: B.Tech CSE\n")
file.close()

print("Data written successfully!")


####################Exception#######################
'''
An exception is an error that occurs during the execution of a program. When an exception occurs, the normal flow of the program is interrupted.
'''
# print(10 / 0)
# print(int("abc"))
# lst = [1,2,3]
# print(lst[4])


try:
    num = int(input("Enter a Number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide number by zero")
except ValueError:
    print("Error: please enter valid number")


print("Here I am ")

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
else:
    print("Division successful!")
    print("Result =", result)

print(10/3)