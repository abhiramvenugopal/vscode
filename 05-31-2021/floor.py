def sumofproduct(n):
    sum=0
    for i in range(n+1):
        val=n//i
        sum+=i*val
    return sum


n = int(input())
print(sumofproduct(n))