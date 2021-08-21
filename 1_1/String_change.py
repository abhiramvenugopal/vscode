def stringChange(str1,str2):
    dict1={}
    dict2={}
    if len(str1)!=len(str2):
        return 0
    for i in range(len(str1)):
        dict1[str1[i]]=dict1.get(str1[i],0)+1
        dict2[str2[i]]=dict2.get(str2[i],0)+1
    for key,value in dict1.items():
        if key not in dict2 or value!=dict2[key]:
            return 0
    return 1


str1=input()
str2=input()
print(stringChange(str1,str2))