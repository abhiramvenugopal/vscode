k=int(input())
n=int(input())
num_list=[]
index=-1
for _ in range(n):
    num_list.append(int(input()))
for j,i in enumerate(num_list):
    if i==k:
        index=j
        break
if index<0:
    print(-1)
else:
    print(index)
