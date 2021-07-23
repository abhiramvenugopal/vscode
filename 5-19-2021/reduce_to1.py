n=int(input())
in_list=[]
for i in range(n):
    in_list.append(int(input()))
for i in in_list:
    if i<=1:
        print(-1)
    else:
        print(1)