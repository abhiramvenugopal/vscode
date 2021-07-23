n,x=map(int,input().split())
num_list=[]
s=0
flag=False
num_list=list(map(int,input().split()))
for i in range(n):
    ar=[]
    for j in range(n):
        if(i!=j):
            ar.append(num_list[j])
    s=sum(ar)
    if s==x:
        flag=True
        break
if flag:
    print(1)
else:
    print(0)

    #    ar=num_list[0:i]+num_list[i+1:]
    # s=sum(ar)
    # if s==x:
    #     flag=True
    #     break