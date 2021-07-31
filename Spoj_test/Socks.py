n=int(input())
arr=[int(i) for i in input().split()]
dict={}
count=0
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for value in dict.values():
    count+=value//2
print(count)
