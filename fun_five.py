def funfive(n):
    count=0
    while n%5==0:
        count+=1
        n=n/5
    return count
for _ in range(int(input())):
    n=int(input())
    i=1
    summ=0
    while(summ<n):
        summ+=funfive(i)
        i+=1
    print(i-1)
