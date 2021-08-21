def productOfelements(arr,n):
    if len(arr)==1:
        return [1]
    left=[]
    prod=1
    for i in arr:
        prod*=i
        left.append(prod)
    right=[0]*n
    prod=1
    for i in range(n-1,-1,-1):
        prod*=arr[i]
        right[i]=prod
    res=[]
    for i in range(n):
        if i==0:
            l=1
            r=right[i+1]
        elif i==n-1:
            r=1
            l=left[i-1]
        else:
            r=right[i+1]
            l=left[i-1]
        res.append(r*l)
    return res
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(*productOfelements(arr,n))
