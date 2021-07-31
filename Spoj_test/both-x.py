def bothCountX(string1, string2, x):
    string1=string1.lower()
    string2=string2.lower()
    dictStr1={}
    dictStr2={}
    res=[]
    for i in string1:
        dictStr1[i]=dictStr1.get(i,0)+1
    for i in string2:
        dictStr2[i]=dictStr2.get(i,0)+1
    for i in dictStr1.keys():
        if (i in dictStr2) and (dictStr1[i]==x) and (dictStr2[i]==x):
            res.append(i)
    res.sort()
    return res


for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))