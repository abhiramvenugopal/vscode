n=int(input())
t=int(input())
t_array=[]
cost_array=[]
total={}
for i in range(n):
    t_array.append(int(input()))
for i in t_array:
    if i in total.keys():
        total[i]=total[i]+int(input())
    else:
        total[i]=int(input())
max_val=max(total.values())
for key in total:
    if (total[key]==max_val):
        print(key)
