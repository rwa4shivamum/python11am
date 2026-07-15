
# # # print(num // 10)
# # # print(num % 10)

# # #count digits 
# # count = 0
# # while(num > 0):
# #     count += 1
# #     num = num // 10

# # print(count)

# #reverse Number
# num = 123456
# temp = 0
# while(num > 0):
#     digit = num%10
#     temp = temp * 10 + digit
#     num = num // 10

# print(temp)

# #temp = 0; num = 123456 (num > 0 )T: digit=6; temp = 0*10 + 6; temp = 6; num = num // 10 ; num = 12345
# #temp = 6; num = 12345 (num > 0 )T: dgit=5; temp = 6*10 + 5; temp = 65; num = num // 10; num = 1234
# #temp = 65; num = 1234 (num > 0 )T: digit=4; temp = 65*10 + 4; temp = 654; num = num // 10; num = 123
# #temp = 654; num = 123 (num > 0 )T: digit=3; temp = 654*10 + 3; temp = 6543

# # print(num // 10)

# # num = 1234
# # product = 1

# # while num > 0:
# #     product *= num % 10
# #     num //= 10

# # print(product)


# #num 1-100 
# num = 9
# count = 0
# i=1
# while(i<=num):
#     if(num%i == 0):
#         count +=1
#     i += 1

# if(count == 2):
#     print("number is prime",num)
# else:
#     print("number is not Prime", num)

# #num=9; count=0;i=1; i<=num; 9%1 == 0 T count +1 count = 1
# #count=1; i=2 2<num; 9%2 == 0 F ; i+1
# #count=1; i=3 3<num; 9%3 == 0 T; count = 2; i+1 = 4;
# #count=2; i=4 4<num; 9%4 == 0 F; count = 2; i=5;
# #count=2; i=5 5<numT; 9%5==0 F; count = 2; i=6;
# #count=2; i=6 6<numT; 9%6==0 F; count = 2; i=7;
# #count=2; i=7 7<
# #count=2; i=9 9<=numT; 9%9==0 T; count = 3


# arr = [4, 8, 2, 10, 6]
# # print(len(arr))
# max = arr[0]
# secondLarge = 0
# i=0
# while (i<len(arr)):
#      if(max < arr[i]):
#          secondLarge = max
#          max = arr[i]
#      i += 1

# print(secondLarge,max)

# #i=0; max = 4; i<5 T; max=4 < 4 F i=1
# #i=1; max = 4; i<5 T; max=4 < 8 T second = 4; max = 8
# #i=2; max = 8; secon = 4; i<5 T; max=8<2 F i=3
# #i=3; max = 8; secon = 4; 3<5 T; max=8<10 T; second = 8; max = 10


# n = 36

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# 153 = 1^3 + 5^3 + 3^3 = 153
# 1634 = 1^4


# i=1
# while(i<10):

#     if(i%2==0):
#         i+=2
#     i+=1