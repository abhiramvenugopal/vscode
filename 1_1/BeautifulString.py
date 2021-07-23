def beautifulString(s):
    aCount=[0]*(len(s)+1)
    bCount=[0]*(len(s)+1)
    cCount=[0]*(len(s)+1)
    for i in range(1,len(s)+1):
        if s[i-1]=="a":
            aCount[i]=aCount[i-1]+1
            bCount[i]=bCount[i-1]
            cCount[i]=cCount[i-1]
        elif s[i-1]=="b":
            aCount[i]=aCount[i-1]
            bCount[i]=bCount[i-1]+1
            cCount[i]=cCount[i-1]
        elif s[i-1]=="c":
            aCount[i]=aCount[i-1]
            bCount[i]=bCount[i-1]
            cCount[i]=cCount[i-1]+1
    print(aCount,bCount,cCount)
beautifulString("abacbcba")