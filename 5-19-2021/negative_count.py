n=int(input())
val_list=list(map(int,input().split()))
count=0
for i in val_list:
    if i<0:
        count+=1
print(count)