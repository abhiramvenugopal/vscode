def binaryInsert(arr,item,l,r):
    while(l<=r):
        mid=l+((r-l)//2)
        if arr[mid]==item:
            return mid
        elif arr[mid]<item:
            l=mid+1
        else:
            r=mid-1
    if arr[mid]<item:
        return mid+1
    return mid


for _ in range(int(input())):
    arr=[int(i) for i in input().split()]
    t=int(input())
    arrInt=[int(i) for i in input().split()]
    for e in arrInt:
        print(binaryInsert(arr,e,0,len(arr)-1))
