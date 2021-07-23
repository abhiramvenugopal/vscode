n,k=[int(i) for i in input().split()]
arr=list(input())
minCount=float('inf')
for i in range(0,n-k+1):
    l=len(set(arr[i:i+k]))
    print(arr[i:i+k])
    if minCount>l:
        minCount=l
print(l)