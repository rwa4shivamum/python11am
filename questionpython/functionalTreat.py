'''
if user 1D array = take value direct
if user 2d array = row, col 2*2=4 , row2nd = 2*2=4

'''

# arr2d = [[1,2,3,4],[1,2,3,4]]
# print(sum(arr2d[0]) + sum(arr2d[1]))
lst = []
def inputArray(lst):
    userInput = int(input("Enter type of Array: "))
    match userInput:
         case 1:
            lst= list(map(int,input("Ente the value by space: ").split(" ")))
            return lst
         case 2:
            rows = int(input("Enter the no. of rows: "))
            cols = int(input("Enter the no. of cols: "))
            valueNeededforSingleList = rows * cols
            for i in range(rows):
                lsts = list(map(int,input(f"Ente the value {valueNeededforSingleList} by space: ").split(" ")))
                lst.append(lsts)
            return lst
print(inputArray(lst))

def dataSummary(lst):
    return f'''
    Data Summary:
    - Total Element:{len(lst)}
    - Minimum value:{min(lst)}
    - Maximum value:{max(lst)}
    - Sum of all Value: {sum(lst)}
    - Average value: {sum(lst)/len(lst)} 
    '''





# values= input("Ente the value by space: ").split(" ")
# lstCompre = [int(i) for i in input("Ente the value by space: ").split(" ")]
# lstCompre1 = list(map(int,input("Ente the value by space: ").split(" ")))
# lstSqare = map(lambda a:a**2,lstCompre1)
# lstofAllnumber = [1,2,3,4,5,6,7]

# lstfilter = list(filter(lambda a:a%2==0,lstofAllnumber))

# lstfilterofEven = []
# for i in range(len(lstofAllnumber)):
#     if lstofAllnumber[i]%2==0:
#         lstfilterofEven.append(lstofAllnumber[i])
    
# print(lstfilter)
# print(values)
# for i in range(len(values)):
#     print(type(values[i]))
#     values[i] = int(values[i])
#     print(type(values[i]))

# lstofAllnumber = [1,2,3,4,5,6,7]

# # lstfilterofEven = []
# # for i in range(len(lstofAllnumber)):
# #     if lstofAllnumber[i]%2==0:
# #         lstfilterofEven.append(lstofAllnumber[i])

# # print(lstofAllnumber,lstfilterofEven)

# lstfolterofEven = list(filter(lambda a:a%2==0,lstofAllnumber))
