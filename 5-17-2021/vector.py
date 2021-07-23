# Vectors
# Given two force vectors, find out whether they are parallel, perpendicular or neither. Let the first vector be A = a1 i +a2 j + a3 k and the second vector be B = b1 i + b2 j + b3 k.

# A.B = a1 x b1 + a2 x b2 + a3 x b3

# A x B = (a2 x b3 - a3 x b2) i - (a1 x b3 - b1 x a3) j + (a1 x b2 - a2 x b1) k

# |A|2 = a12 + a22 + a32

# If A.B = 0, then A and B are perpendicular.

# If |A X B| = 0, then A and B are parallel.

# Input
# First line contains three space seperate values denoting, a1, a2, a3 respectively. Second line contains three space seperate values denoting, b1, b2, b3 respectively.

# Output
# Print 1 if they are parallel to each other, 2 if they are perpendicular to each other or 0 otherwise.

# Example
# Input1:

# 3 2 1
# 6 4 2
# Output1:

# 1
# Explanation:

# |A X B| = 0




# ----------------------------------------------------------------------------------------


a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_dot_b = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
a_cross_b = [(a[1] * b[2] - a[2] * b[1]) ,(a[0] * b[2] - b[0] * a[2])*-1 , (a[0] * b[1] - a[1] * b[0])]
mod_a_cross_b=(a_cross_b[0]**2)+(a_cross_b[1]**2)+(a_cross_b[2]**2)

if(mod_a_cross_b==0):
    print(1)
elif(a_dot_b==0):
    print(2)
else:
    print(0)
