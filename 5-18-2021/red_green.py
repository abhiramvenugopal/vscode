# Input
# One String.

# Output
# One Integer, denoting the minimum number of characters you need to change to make the whole string of the same colour.

# Example
# Input1:

# RGRGR
# Output1:

# 2
# Explanation:

# We need to change only the 2nd and 4th(1-index based) characters to 'R', so that the whole string becomes the same colour.


# ------------------------------------------------------------------------------------


str_in=input()
r_count=str_in.count("R")
g_count=str_in.count("G")
if r_count>=g_count:
    print(str_in.count("G"))
else:
    print(r_count)