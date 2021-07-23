# Series
# Given a number N, find the N-th term in the series 1, 3, 6, 10, 15, 21...

# Input
# One integer, denoting N.

# Output
# One Integer, denoting the N-th term in the series 1, 3, 6, 10, 15, 21....

# Example
# Input1:

# 4
# Output1:

# 10
# Input2:

# 3
# Output2:

# 6

# --------------------------------------------------------------------------------

n=int(input())
start=1
for i in range(2,n+1):
    start+=i
print(start)
