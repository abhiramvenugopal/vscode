# maximum number of submissions: 10
# Single Number
# Given a list of N integers, every element appears twice except for one. Find that single one.

# Input
# First number is N (the number of integers given) Followed by the N numbers

# Output
# One line containing the output integer

# Example
# Input: 3 2 2 1

# Output: 1

# Input: 5 2 2 1 1 3

# Output: 3


# ----------------------------------------------------------------------------------

# num_list=input().split()[1:]
# for i in num_list:
#     if num_list.count(i)==1:
#         print(int(i))

# bestsolution

num_list=list(map(int,input().split()[1:]))
res=0
for i in num_list:
    res^=i
print(res)
