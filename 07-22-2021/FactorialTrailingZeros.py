def trailingZeroes(n):
    if n==0:
        return 1
    return n//5

# DO NOT CHANGE ANYTHING BELOW THIS LINE
num_tests=int(input())
for _ in range(num_tests):
    n=int(input())
    print(trailingZeroes(n))