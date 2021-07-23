n=int(input())
string_list=list(map(str,input().split()))
string_list=list(sorted(string_list,key=len))
print(len(string_list[n-1]))    