n,x=map(int,input().split())
count=0
num_list=list(map(int,input().split()))
for i in num_list:
    if i%x==0:
        count+=1
print(count)