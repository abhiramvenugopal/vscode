import copy

# shallow copy
print(" shallow copy")
l=[1,2,3,4,5,6,[1,2,3]]
m=l.copy()

m[3]=88

m[-1][0]=99
print(l)
print(m)


# deep copy


print("deep copy")
l=[1,2,3,4,5,6,[1,2,3]]
m=copy.deepcopy(l)

m[3]=88

m[-1][0]=99
print(l)
print(m)
