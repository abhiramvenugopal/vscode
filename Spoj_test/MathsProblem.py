def gcd(a,b):
    while (a%b!=0):
        temp=a
        a=b
        b=temp%b
    return b
for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    a,b=[a,b] if a>=b else [b,a]
    print(gcd(a,b))