str = ["aaabbbbcccc", "cccdd"]
output = []

for word in str:
    result = "" #a3b2
    count = 1

    for i in range(1,len(word)):
        if(word[i] == word[i - 1]):
            count += 1
        else:
            result += word[i - 1] + f"{count}"
            count = 1
    
    result += word[-1] + f"{count}"
    print(result)
    output.append(result) 

print(output)
#word = "aaabb", result="", count = 1, 
#i=1, if(word[i]=a == word[i-1]=a): count = 2
#i=2, if(word[2]=a == word[2-1]=1): count = 3
#i=3, if(word[3]=b !== )F result = "a3", count = 1
#i=4, if(word[4]=b == word[4-1]=b)T; count = 2
#i=5<5 F
#result += "a3" + "b2" + 2
#result = "a3b2"
# output.append(result)
# output=["a3b2"]



# str1 = 1231
# str2 = str(str1)
# print(str(str1))
# print(type(str2))

str1 = "anjkand"
print(str1[-1])