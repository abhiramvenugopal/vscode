def substr(arr,k,n,s,pos,collect):
    if len(s)==k:
        collect.append(s)
        return
    else:
        if pos<n:
            substr(arr,k,n,s+arr[pos],pos+1,collect)
            substr(arr,k,n,s,pos+1,collect)
            

n,k=[int(i) for i in input().split()]
collect=[]
arr=list(input())
substr(arr,k,n,"",0,collect)
collect.sort()
for i in collect:
    print(i)
