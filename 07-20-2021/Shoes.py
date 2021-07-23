n=int(input())
arr=[int(i) for i in input().split()]
dict={}
total=0
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for _ in range(int(input())):
    size,amount=[int(e) for e in input().split()]
    if not (size not in dict or dict[size]==0):
        total+=amount
        dict[size]-=1
print(total)
