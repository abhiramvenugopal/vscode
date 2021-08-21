def createDict(S):
    dict={}
    for c in S:
        dict[c]=dict.get(c,0)+1
    return dict
def groupAnagrams(strs):
    if len(strs)==0:
        return [[""]]
    dictarr=[]
    res=[]
    for s in strs:
        dicts=createDict(s)
        if len(res)==0:
            res.append([s])
            dictarr.append(dicts)
        else:
            flag=True
            for i in range(len(dictarr)):
                secflag=True
                for c in dicts:
                    if c not in dictarr[i] or dicts[c]!=dictarr[i][c]:
                        secflag=False
                        break
                if secflag:
                    res[i].append(s)
                    flag=False
                    break
            if flag:
                res.append([s])
                dictarr.append(dicts)
    for i in res:
        i.sort()
    res.sort(key=lambda x:x[0])
    res.sort(key=len)
    return res


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))