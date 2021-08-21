def findGroups(arr,n):
    if n<=1:
        return n
    count=1
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            count+=1
    return count
n=int(input())
arr=[int(i) for i in input().split()]
print(findGroups(arr,n))

