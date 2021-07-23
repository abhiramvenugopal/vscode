n=int(input())
arr=[int(i) for i in input().split()]
dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
maxval=-1
maxindex=-1
for key,value in dict.items():
    if value>maxval:
        maxval=value
        maxindex=key
    elif value==maxval and maxindex>key:
        maxindex=key
print(maxindex)
