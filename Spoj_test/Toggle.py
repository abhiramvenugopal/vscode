def toggle(S):
    res=""
    for c in S:
        if ord(c)<=90:
            res+=chr(ord(c)+32)
        else:
            res+=chr(ord(c)-32)
    print(res)
toggle(input())