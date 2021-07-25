def compareVersion(version1,version2):
    v1=[int(i) for i in version1.split(".")]
    v2=[int(i) for i in version2.split(".")]
    diff=len(v1)-len(v2)
    if diff>0:
        v2=v2+[0]*diff
    elif diff<0:
        v1=v1+[0]*diff
    for i in range(len(v1)):
        if v1[i]<v2[i]:
            return -1
        elif v1[i]>v2[i]:
            return 1
    return 0


for _ in range(int(input())):
    version1,version2=[i for i in input().split()]
    print(compareVersion(version1,version2))