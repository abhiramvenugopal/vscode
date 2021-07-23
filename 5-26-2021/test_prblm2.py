n,k=map(int,input().split())
crakers_list=[0]*k
min=n
max=0
for i in range(n):
    crakers_list[i%k]+=1
for j in crakers_list:
    if j<min:
        min=j
    if j>max:
        max=j
print(max-min)