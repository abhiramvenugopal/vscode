def compress(st):
    res=""
    count=1
    item=st[0]
    for i in range(1,len(st)):
        if st[i]==item:
            count+=1
        else:
            if count==1:
                res+=item
            else:
                res+=item+str(count)
            item=st[i]
            count=1
    if count==1:
        res+=item
    else:
        res+=item+str(count)
        item=st[i]
        count=1
    print(res)

t = int(input())
for _ in range(t):
    st = input()
    compress(st)