n=int(input())
input_list=[]
sum_list=[]
for _ in range(n):
    num1=input().split()
    num2=input().split()
    input_list.append([num1,num2])
for i in input_list:
    sum=""
    rem=0
    for k,m in zip(i[0],i[1]):
        s=int(k)+int(m)+rem
        sum=sum+str(s%10)
        rem=s//10
    if len(i[0])>len(i[1]):
        for j in i[0][len(i[1]):]:
            s=int(j)+rem
            sum=sum+str(s%10)
            rem=s//10
    elif len(i[0])<len(i[1]):
        for j in i[1][len(i[0]):]:
            s=int(j)+rem
            sum=sum+str(s%10)
            rem=s//10
    if(rem!=0):
        sum=sum+str(rem)
    print(sum)