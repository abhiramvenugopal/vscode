# Count odd even numbers
# Count number of odd and even number in given list.

# Input
# First line contains length of the list. Each line contains integer specifying each element in list.

# Output
# 2 integers in each line specifying count of odd and even numbers respectively.

# Example
# Input:

# 5

# 12

# 14

# 15

# 13

# 18

# Output:

# 2

# 3

# -------------------------------------------------------------


odd_count=0
even_count=0
n=int(input())
for i in range(n):
    val=int(input())
    if(val%2==0):
        even_count+=1
    else:
        odd_count+=1
print(odd_count)
print(even_count)