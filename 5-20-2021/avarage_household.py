n=int(input())
income_list=[]
child_list=[]
count=0
sum=0
for i in range(n):
    income_list.append(int(input()))
for i in range(n):
    child_list.append(int(input()))
for i,j in zip(income_list,child_list):
    if(j>2):
        sum+=i
        count+=1
if count:
    print(sum//count)
else:
    print(-1)
