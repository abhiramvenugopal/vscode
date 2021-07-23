# Given an integer, reverse digits of an integer

# Input
# 1 line containing the integer to reverse

# Output
# 1 line containing the reversed integer

# Example
# Input: 123

# Output: 321

# Input: 120

# Output: 21 because starting 0 can be removed

# Input: -123

# Output: -321
# --------------------------------------------------------------------------------------

num=int(input())
if(num<0):
    print(int(str(abs(num))[::-1])*-1)
else:
    print(int(str(num)[::-1]))