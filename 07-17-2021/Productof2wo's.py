n=int(input())
arr=[int(i) for i in input().split()]
summ=0
for j in arr:
    summ+=abs(j)
abssum=0
for i in arr:
    abssum+=abs(i)*(summ-abs(i))
print(abssum)
