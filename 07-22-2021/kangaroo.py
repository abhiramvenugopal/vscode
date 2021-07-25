for _ in range( int(input()) ):
    x1,v1,x2,v2=[int(i) for i in input().split()]
    if x1==x2:
        print("YES")
        continue
    if x1>=x2 and v1>v2 or x1<=x2 and v1<v2:
        print("NO")
        continue
    diff=abs(abs(x2-x1)-abs((x1+v1)-(x2+v2)))
    if diff==0:
        print("NO")
        continue
    diff=(abs(x2-x1))//diff
    if x1+(diff*v1)==x2+(diff*v2):
        print("YES")
        continue
    else:
        print("NO")

