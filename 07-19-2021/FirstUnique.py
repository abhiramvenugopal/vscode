def firstUnique(S):
    dict={}
    for c in S:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1
    for i in range(len(S)):
        if dict[S[i]]==1:
            return i
    print(dict)
    return -1

for _ in range(int(input())):
    S=input()
    print(firstUnique(S))