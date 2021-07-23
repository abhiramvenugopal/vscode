n=int(input())
in_list=[]

mono_flag_pos=True
mono_flag_neg=True
for i in range(n):
    in_list.append(int(input()))
for i in range(1,n):
    if in_list[i-1]>in_list[i] and mono_flag_pos:
        mono_flag_pos=False
    if in_list[i-1]<in_list[i] and mono_flag_neg:
        mono_flag_neg=False

print(mono_flag_neg or mono_flag_pos)
