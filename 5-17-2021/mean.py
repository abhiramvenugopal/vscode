# Mean
# Given the marks of N students in an Array A, calculate the mean.

# Note: If result is a Decimal Value, find it's floor Value.

# Constraints:
# 1 <= N <= 6
# Input
# One integer, denoting N, the length of the array A. Next line denotes N space seperated integers, denoting the elements of the array

# Output
# One Integer, denoting the required mean.

# Example
# Input:

# 4
# 56 67 30 79
# Output:

# 58
# Explanation:

# 56+67+30+79 = 232;  232/4 = 58.
# So, the Output is 58.

# ---------------------------------------------------------------------------------------------

n=int(input())
num_list=list(map(int,input().split()))
mean=0
for i in num_list:
    mean+=i
print(mean//n)
