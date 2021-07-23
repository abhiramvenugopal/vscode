n=int(input())
num_list=list(map(int,input().split()))
sum=0
for i in range(0,n,2):
    sum+=num_list[i]
print(sum)