def anagram(s1:str,s2:str):
    dict1={}
    dict2={}
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        dict1[s1[i]]=dict1.get(s1[i],0)+1
        dict2[s2[i]]=dict2.get(s2[i],0)+1
    for c in dict1:
        if c not in dict2 or  dict1[c]!=dict2[c]:
            return False
    return True
for _ in range(int(input())):
    s1,s2=input().split()
    print(anagram(s1,s2))