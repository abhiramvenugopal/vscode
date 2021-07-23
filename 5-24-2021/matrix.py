n,m=map(int,input().split())
matrix_list=[]
sum=0
for _ in range(n):
    matrix_list.append(list(map(int,input().split())))
for i in matrix_list:
    for j in i:
        if j%2!=0:
            sum+=j
print(sum)