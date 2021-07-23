n=int(input())
val_list=list(map(int,input().split()))
sum=0
for i in val_list:
    if i%2==0:
        sum+=i
print(sum)