n,k=map(int,input().split())
num_list=[int(i) for i in input().split()]
count=0
for i in num_list:
    if i==k:
        count+=1
print(count)
