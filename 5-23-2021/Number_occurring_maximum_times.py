n=int(input())
num_list=[]
count=1
val=-1
for _ in range(n):
    num_list.append(int(input()))
prev=num_list[0]
for i in range(1,n):
    if num_list[i]==prev:
        prev=num_list[i]
        count+=1
        if(count==4):
            val=num_list[i]
            break
    else:
        prev=num_list[i]
        count=1
print(val)
