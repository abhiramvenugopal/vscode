n=int(input())
num_list=[]
for i in range(n):
    num_list.append(int(input()))
query_int=int(input())
print(num_list.count(query_int))