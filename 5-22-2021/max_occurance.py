n=int(input())
num_list=[]
item=[]
count=[]
for _ in range(n):
    num_list.append(int(input()))
for i in num_list:
    for j in num_list:
        if i==j:
            if i not in item:
                item.append(i)
                count.append(1)
            else:
                count[item.index(i)]+=1
if len(item)==0:
    print(-1)
else:
    max_val=max(count)
    for i in range(len(item)):
        if count[i]==max_val:
            print(item[i])
