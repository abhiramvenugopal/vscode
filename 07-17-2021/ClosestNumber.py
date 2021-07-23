def binaryInsert(arr,item,l,r):
    while(l<=r):
        mid=l+((r-l)//2)
        if arr[mid]==item:
            return mid
        elif arr[mid]<item:
            l=mid+1
        else:
            r=mid-1
    # if arr[mid]<item:
    #     return mid+1
    return mid


n,q=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
qs=[int(i) for i in input().split()]
for e in qs:
    print(arr[binaryInsert(arr,e,0,n-1)],end=" ")
