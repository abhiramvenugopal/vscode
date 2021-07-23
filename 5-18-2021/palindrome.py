in_str=input()
n=int(input())
if len(in_str)==1:
	print(in_str)
elif n==0:
    print(in_str+in_str[::-1])
else:
    print(in_str+in_str[-2::-1])