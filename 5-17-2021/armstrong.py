# For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. Print Yes if it is a armstrong number else print No.

# Input
# One integer, denoting the 3 digit number.

# Output
# One string, denoting Yes or No.

# Example
# Input1:

# 153
# Output1:

# Yes
# Explanation:

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153



# -------------------------------------------------------------------------------------




n=input()
sum=0
for i in n:
    sum+=int(i)**len(n)
if sum==int(n):
    print("Yes")
else:
    print("No")