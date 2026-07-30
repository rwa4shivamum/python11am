# 1.orderd
# 2.immutable
# 3.Hetrogenous
# 4.indexing and slicing
# 5. nested tuple
# 6. memory efficient
# 7.denoted by ()

#       0   1     2      3      4
tupl = (1,True,"string",3.2,(1,2,3,43),1,1,1)
# tupl[0] = 3
print(tupl[0])
print(tupl[4][3])

# lst = [1,2,3,4,[12,3,3,4,53,[1,32,3,4,4]]]
# print(lst[4][5][1])

# tuple methods
# print(dir(tupl))
print(tupl.count(1))       
print(tupl.index("string"))