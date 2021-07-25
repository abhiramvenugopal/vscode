def modPallindrome(S):
    if S[::-1]==S:
        return True
    else:
        l=0
        r=len(S)-1
        while(l<=r):
            if S[l]!=S[r]:
                modstr=S[:l]+S[l+1:]
                if modstr==modstr[::-1]:
                    return True
                modstr=S[:r]+S[r+1:]
                if modstr==modstr[::-1]:
                    return True
                return False
            else:
                l+=1
                r-=1
for _ in range(int(input())):
    S=input()
    print(modPallindrome(S))
    
