def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
n=int(input())
arr=[int(i) for i in input().split()][:n]
time=arr[0]
for i in range(1,n):
    time=lcm(time,arr[i])
print(time)