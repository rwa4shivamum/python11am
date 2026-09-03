matrix = [
          [1,2,3],
          [4,5,6]
                ]
'''
o/p
[
 [1,4]
 [2,5]
 [3,6]
]
[[1, 4, 3], 
 [2, 5, 6]]
'''
def transposeMatrix(matrix):
    i=0 #row
    j=0 #col
    rowLength = len(matrix)
    colLength = len(matrix[0])
    while(i<rowLength and j<colLength):
        print("I am here")
        if(i != j ):
            print("I am here 2")
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            i += 1
            j += 1
        else:
            i += 1

    return matrix

print(transposeMatrix(matrix)) 

