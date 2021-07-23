a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
alice=0
bob=0
for i in range(3):
    if a[i]==b[i]:
        continue
    elif a[i]>b[i]:
        alice+=1
    else:
        bob+=1
print(alice,bob)