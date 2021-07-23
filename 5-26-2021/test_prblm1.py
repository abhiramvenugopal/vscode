a,b=map(int,input().split())
a,b= [a,b] if a<b else [b,a]
flag=False
for i in range(a,b+1):
    if (a*b*i)%2!=0:
        flag=True
        break
if flag:
    print("Yes")
else:
    print("No")