import math
def findHeight(a,b):
    return math.ceil((2*a)/b)
for _ in range(int(input())):
    b,a=[int(i) for i in input().split()]
    print(findHeight(a,b))

