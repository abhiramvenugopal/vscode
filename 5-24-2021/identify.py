str_in=input()
int_list=[1,2,3,4,5,6,7,8,9,0]
count=0
for i in str_in:
    if not i.isalpha():
        count+=1
print(count)