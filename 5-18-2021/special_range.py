    m=int(input())
    n=int(input())
    m= 0 if m<=0 else m
    n= 0 if n<=0 else n

    if m>=n:
        print(-1)
    else:
        for i in range(m,n+1):
            print(i)