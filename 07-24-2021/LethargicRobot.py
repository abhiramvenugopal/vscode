# def lethargicRobot(n,S,leftcount,rightcount,collect):
#     if leftcount == rightcount and len(S)==n:
#         collect.append(S)
#     elif len(S)<n:
#         lethargicRobot(n,S+"L",leftcount+1,rightcount,collect)
#         lethargicRobot(n,S+"R",leftcount,rightcount+1,collect)
#         lethargicRobot(n,S+"S",leftcount,rightcount,collect)
# n=int(input())
# collect=[]
# lethargicRobot(n,"",0,0,collect)
# print(len(collect))
import math


def lethargicRobot(n):
    lrmaxx=n//2
    summ=0
    nfact=math.factorial(n)
    for i in range(lrmaxx+1):
        scount=n-(2*i)
        ifact=math.factorial(i)
        scountfact=math.factorial(scount)
        if scount!=0:
            if scount!=n:

                val=(nfact)//(ifact*ifact*scountfact)
                summ+=val
            else:
                summ+=1
        else:
            summ+=(nfact)//(ifact*ifact)
    print(summ)




n=int(input())
lethargicRobot(n)