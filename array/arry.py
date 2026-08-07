#Array -> collection of same data types element
#list -> collection of same and multiple data types

lst = [1,2,3,4,5] #list , array
lst = [1,2,True,"str"] #list, not array

'''
Basic Level
Find the sum of all elements in a 1D array.
Find the maximum and minimum element.
Count how many even and odd numbers are present.
Calculate the average of array elements.
Reverse the given array.
Intermediate Level
Search for a given element and return its index.
Remove duplicate elements from the array.
Sort the array in ascending and descending order.
Find the second largest element.
Count frequency of each element in the array.
Advanced Level
Find all elements greater than a given value (filtering).
Rotate the array by k positions (left/right).
Find the missing number in a sequence.
Check if the array is a palindrome.
'''

lst = [1,2,3,4,5]
# for i in lst:
#     print(i)


# sumOfAllElem = 0
# for i in lst:
#     sumOfAllElem += i
#     print(sumOfAllElem)

# userInputIndex = int(input("Enter the Position of elemen"))
# element = int(input("Enter a num Or element: "))

# lst.insert(userInputIndex-1,element)

print(lst)

# inputValueOfele = int(input("Enter the value from lst: "))
# index = lst.index(inputValueOfele)
# print(index)
# del lst[index]
# print(lst)

# inputValueOfele = int(input("Enter the value from lst: "))
# inputUpdateValue = int(input("Enter the value to Update with: "))
# index = lst.index(inputValueOfele)
# lst[index] = inputUpdateValue

# print(lst)
# inputValueOfele = int(input("Enter the value from lst: "))
# for i in range(len(lst)):
#     if inputValueOfele == lst[i]:
#         print(i)


def returnIndex(lst):
    '''
    This function find element from array and return it's index, 
    if not found then return 'Element not found'
    parameter:
    i.list of integer

    return indexValue if Found
    '''
    value = int(input("Enter a number: "))
    for i in range(len(lst)):
        # print(lst[i], value, type(lst[i]), type(value))
        if(value == lst[i]):
            return i
    return "Element Not Found"

# lst = [1,2,3,4,5]
# print(returnIndex(lst))


lst2 = [6,7,8,9,5,6]
print(len(lst2)//2)
print(lst + lst2)


# 1D = 1 dimensional
# 2D = 2 dimensional
# 3D = 3 dimensional

arr2d = [
         [1,2,3,4],
         [1,2,3,4]
         ]

# arr3d = [
#     [
#         [1,2,3,4]
#     ]
# ]