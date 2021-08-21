def check(msgrcd,msggsd):
    msgrcdDict={}
    msggsdDict={}
    for c in msgrcd:
        msgrcdDict[c]=msgrcdDict.get(c,0)+1
    for c in msggsd:
        msggsdDict[c]=msggsdDict.get(c,0)+1
    for key,value in msggsdDict.items():
        if key not in msgrcdDict or msgrcdDict[key]!=value:
            return "NO"
    return "YES"
for _ in range(int(input())):
    msgrcd=input().lower()
    msggsd=input().lower()
    print(check(msgrcd,msggsd))

