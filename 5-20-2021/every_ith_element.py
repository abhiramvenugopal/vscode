n=int(input())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
step_val=int(input())
sum=0
for i in num_list[step_val-1::step_val]:
    sum+=i
print(sum)