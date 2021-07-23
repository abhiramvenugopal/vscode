block_model=["L","M","U","L","M","U","SL","SU"]
n=int(input())
input_list=[]
for _ in range(n):
    input_list.append(list(map(int,input().split())))
for item in input_list:
    if item[0]<item[1]:
        print("Invalid")
    else:
        print(block_model[(item[1]-1)%8])