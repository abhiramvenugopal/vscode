trib_list=[0,0,1]
n=int(input())
for i  in range(3,n):
    trib_list.append(trib_list[i-1]+trib_list[i-2]+trib_list[i-3])
if n==0 or n==1:
    print(0)
else:
    print(trib_list[-1])