# Consecutive characters
# Given a string S, find the maximum length of a non-empty substring that contains only one unique character. If such a string doesnt exist, return 0

# Input
# one line containing the string S

# Output
# one line containing the maximum length of the substring

# Example
# Input: beet

# Output: 2 Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Input: abbcccddddeeeeedcba

# Output: 5 Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

# Input: triplepillooooow

# Output: 5 Explanation: The substring "ooooo" is of length 5 with the character 'o' only.

# Input: abc

# Output: 1 Explanation: All characters are single characters and not repeated consecutively




# --------------------------------------------------------


max=1
str_in=input()
count=1
for i in range(1,len(str_in)):
    if str_in[i-1]==str_in[i]:
        count+=1
        if count>max:
            max=count
    else:
        count=1
print(max)