def sumofdivisors(n):
    incr=1 if n%2==0 else 2
    sum=0
    for i in range(1,n+1,incr):
        if n%i==0:
            sum+=i
    return sum

n = int(input())
print(sumofdivisors(n))