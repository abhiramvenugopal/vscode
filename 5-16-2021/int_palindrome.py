# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward

# Input
# 1 containing integer

# Output
# 1 line containing Boolean value

# Example
# Input: 121

# Output: True

# Input: 10

# Output: False


# -----------------------------------------------------------------------


n=int(input())
print(n==int(str(n)[::-1]))