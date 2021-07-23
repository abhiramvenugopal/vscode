# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.


class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        max=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count=count+1
                if count>max:
                    max=count
            else:
                count=1
        return max