#????0
#???10
#??101
#?0101
#01010

# ****
# ***
# **
# *
n=5
isTrue=True
for i in range(n,0,-1):
    for j in range(0,i-1):
        print(" ", end="")
    for z in range(0,n-i+1):
        print("0" if isTrue else "1", end="")
        isTrue = not isTrue
    print(" ")

#n=5
#i=5; 5>0 T;
#j=0; j<4 T;j=1
#j=1; j<4 T;j=2
#j=3; 3<4 T;j=4
#j=4; 4<4 F
#z=0; 0<n-i+1(5-5+1) T; 
#z=1; 1<1 F

#i=4
#j=0 to <4

# print("Hello", end=" ")
# print("Hii")



#????*
#???**


#    


# isOn = False
# isOn = not isOn
# print(isOn)

