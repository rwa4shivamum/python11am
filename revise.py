print("Hello")
# name1="shioa"
# name2="kjbd"
# name3="jkb"
# name4="jkbd"

#collection of data (mutable=:data can be change), (it allows to store duplicate value), (orderd Way stored)
#list    0       1           2       3
# lst = ["kjasd", "kjsdf", "kjsbdf", "kjsdf"]
# print(lst[-1])



#Find the first duplicate element.
lst = [1,2,3,4,4,3,4,5]
# print(len(lst))
n = len(lst)
isFind = False
for i in range(0,n):
    for j in range(i+1,n):
        if(lst[i] == lst[j]):
            isFind = True
            print(lst[i])
            if(isFind == True):
                break
    if(isFind == True):
        break


for i in range(0,n):
    for j in range(i+1,n):
        print(i,j)

# 7+6+5+4+3+2+1
# n=8 n^2=64 logn