def misMatchedPair(arr,n):
    arr.sort()
    l=0
    r=n-1
    minn=float('inf')
    rmin=-1
    lmin=-1
    while(l<r):
        if abs(arr[l]+arr[r])<minn:
            lmin=l
            rmin=r
            minn=abs(arr[l]+arr[r])
        elif abs(arr[l]+arr[r])==minn and ((abs(arr[l])+abs(arr[r]))>(abs(arr[lmin])+abs(arr[rmin]))):
            lmin=l
            rmin=r
        if l<n-1 and abs(arr[l+1]+arr[r])<=minn:
            l+=1
        if r>0 and abs(arr[l]+arr[r-1])<=minn:
            r-=1
        else:
            break
    print(arr[lmin],arr[rmin], abs(arr[lmin]+arr[rmin]))
n=int(input())
arr=[int(i) for i in input().split()]
misMatchedPair(arr,n)

