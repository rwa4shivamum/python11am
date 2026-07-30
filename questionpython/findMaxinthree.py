# a=9
# b=10
# c=76

# if(a > b):
#     if(a > c):
#         print("a is graeter")
#     else:
#         print("c is greater")
# elif(b > a):
#     if(b > c):
#         print("b is greter")
#     else:
#         print("c is greatest")
# elif(a > c):
#     if(a > b):
#         print("a is greatest")
#     else:
#         print("b is greatest")
# else:
#     print("all are equal")



# for i in range(51):
#     if(i%2==0 and i%3==0):
#         print("both")
#     elif(i%2==0):
#         print("divibly by 2")
#     elif(i%3==0):
#         print("divisible by 3")

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("")

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

#1 2 3 4 5
#2 3 4 5
n=5
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=" ")
    print("")

#i=5; j=5 5<6 T; j=6 6<6 F;
#i=4; j=4 4<6 T; j=5 5<6 T; j=6 6<6 F;
#i=3; j=3 to 5
#i=2; j=2 to 5




#5
#4 5
#3 4 5
#2 3 4 5
#1 2 3 4 5


str1 =  "hello world"
str2 = str1.split()
str3 = str2[0][1:-1],str2[1][1:-1]