str_list=input().split()
str_list=sorted(str_list,key=len)
print(len(str_list[-1]))