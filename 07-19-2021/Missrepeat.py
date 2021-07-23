n=int(input())
arr=[int(i) for i in input().split()]
i=0
while i<n:
    if arr[i]!=i+1:
        if arr[arr[i]-1]!=arr[i]:
            arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
        else:
            repeat=arr[i]
            i+=1
    else:
        i+=1
for i in range(n):
    if arr[i]!=i+1:
        missing=i+1
        break
print(repeat,missing)
