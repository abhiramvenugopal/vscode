def binarySearch(arr,item):
    l=0
    r=len(arr)-1
    while (l<=r) :
        mid=l+((r-l)//2)
        if arr[mid]==item:
            return mid
        elif item<arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1
for _ in range(int(input())):
    arr=[int(i) for i in input().split()]
    n=int(input())
    toFindElements=[int(i) for i in input().split()]
    for i in range(n):
        print(binarySearch(arr,toFindElements[i]))