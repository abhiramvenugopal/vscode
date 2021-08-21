def findValue(s):
    if len(s)==0:
        return 0
    else:
        return int(s[0])+findValue(s[1:])
s=input()
print(findValue(s))