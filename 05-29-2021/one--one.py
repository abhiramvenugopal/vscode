# # given a string - find a sub sequance "abc"
# # bcdabfc-Yes
# # bcdbafc-No

# str_in=input()
# seq="abc"
# counter=0
# flag=True
# for i in str_in:
#     if seq[counter]==i:
#         counter+=1
#     if counter==3:
#         print("Yes")
#         flag=False
#         break
# if flag:
#     print("No")


# given array of numbers - given range l,r - 
# [1,7,8,12,15] l=9 r=13-yes

num_list=list(map(int,input().split()))
l,r=map(int,input().split())
flag=True
left=0
right=len(num_list)-1
while(left<=right):
    m=(left+right)//2
    if num_list[m]>=l and num_list[m]<=r:
        flag=False
        print("Yes")
        break
    elif num_list[m]<r:
        left=m+1
    else:
        right=m-1
if flag:
    print("No")