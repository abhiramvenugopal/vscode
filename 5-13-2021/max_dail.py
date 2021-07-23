n=int(input())
valArray=[0]*n
max=int(input())
m=int(input())
flag=False
iArray=[]
for j in range(m):
    iArray.append(int(input()))
for i in iArray:
    valArray[i-1]+=1
    if(valArray[i-1]==max):
        print(i)
        flag=True
        break
if(not flag):
    print(0)