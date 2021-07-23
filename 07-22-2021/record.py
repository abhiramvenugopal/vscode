n=int(input())
arr=[int(i) for i in input().split()]
minn=arr[0]
maxx=arr[0]
low=0
high=0
for i in range(1,n):
    if arr[i]<minn:
        minn=arr[i]
        low+=1
    elif arr[i]>maxx:
        maxx=arr[i]
        high+=1
print(high,low)