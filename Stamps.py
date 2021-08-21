def findMaxNoOfDifferentStamp(arr,n):
    s=set(arr)
    if len(s)>n//2:
        return n//2
    else:
        return len(s)
n=int(input())
arr=[int(i) for i in input().split()]
print(findMaxNoOfDifferentStamp(arr,n))