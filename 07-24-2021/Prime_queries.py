n,q=[int(i) for i in input().split()]

countarr=[0]*(n+1)
arr=[True]*(n+1)
arr[0]=False
arr[1]=False
p=2
count=0
while(p*p<=n+1):
    if arr[p]:
        count+=1
        for i in range(p*p,n+1,p):
            arr[i]=False
    countarr[p]=count
    p=p+1
for i in range(p,n+1):
    if arr[i]:
        count+=1
    countarr[i]=count

for _ in range(q):
    num=int(input())
    print(countarr[num])