def lengthOfLongestSubstring( s: str) -> int:
    l=len(s)
    while(l>0):
        for i in range(len(s)-l+1):
            print(i,i+l)
            sam=s[i:i+l]
            status=True
            print(sam)
            for i in sam:
                if(sam.count(i)>1):
                    status=False
                    break
            if(status):
                return len(sam)
        l=l-1
s="pwwkew"
print(lengthOfLongestSubstring(s))
