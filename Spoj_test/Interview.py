femaleArr=[]
maleArr=[]
for _ in range(int(input())):
    mf,tl=[int(i) for i in input().split()]
    if mf==0:
        femaleArr.append(tl)
    else:
        maleArr.append(tl)
femaleArr.sort(reverse=True)
maleArr.sort(reverse=True)
res=femaleArr+maleArr
print(*res)
