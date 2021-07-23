n=int(input())
num_list=list(map(int,input().split()))
num_list=sorted(num_list)
print(num_list[-1]-num_list[0])