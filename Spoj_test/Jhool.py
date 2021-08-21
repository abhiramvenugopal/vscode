def rubyCount(S):
    dict={'r':0,'u':0,'b':0,'y':0}
    for c in S:
        if c in dict:
            dict[c]+=1
    minval=min(dict,key=dict.get)
    print(dict[minval])
for _ in range(int(input())):
    rubyCount(input())