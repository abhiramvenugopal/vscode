dict={}
i=0
for val in input().split():
    dict[chr(97+i)]=int(val)
    i+=1
S=input()
maxx=-1
for c in S:
    if dict[c]>maxx:
        maxx=dict[c]
print(len(S)*1*maxx)
