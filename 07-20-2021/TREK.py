def countValley(S):
    level=0
    count=0
    flag=False
    for c in S:
        if c =="U":
            level+=1
        else:
            level-=1
        if flag and level==0:
            count+=1
        flag=(level<0)
    print(count)

for _ in range(int(input())):
    n=int(input())
    S=input()
    countValley(S)
