def longestSubstring(S):
    dict={}
    i=0
    j=0
    maxx=0
    while j<len(S):
        if S[j] not in dict:
            if (j-i+1)>maxx:
                maxx=j-i+1
            dict[S[j]]="item"
            j+=1
        else:
            while(S[j] in dict):
                dict.pop(S[i])
                i+=1
    return maxx
for _ in range(int(input())):
    S=input()
    print(longestSubstring(S))

