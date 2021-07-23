def fun(S):
    dict={}
    count=0
    countNum={}
    for i in S:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    flag=True
    dictValues={}
    for value in dict.values():
        if value in dictValues:
            dictValues[value]+=1
        else:
            dictValues[value]=1
        if len(dictValues)>2:
            return False
    for value in dictValues.values():
        if value>1:
            count+=1
    if count>1:
        return False
    return True
        
n=int(input())
S=input()
print(fun(S))

