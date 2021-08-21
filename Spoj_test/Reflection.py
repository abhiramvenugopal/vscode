def findRef(p,q):
    print(p,q)
    r=[]
    if p[0]==q[0]:
        r=[0,(q[1]+(q[1]-p[1]))]
    elif p[1]==q[1]:
        r=[(q[0]+(q[0]-p[0])),0]
    else:
        r=[(q[0]+(q[0]-p[0])),(q[1]+(q[1]-p[1]))]
    return r
for _ in range(int(input())):
    px,py,qx,qy=[int(i) for i in input().split()]
    res=findRef([px,py],[qx,qy])
    print(*res)
