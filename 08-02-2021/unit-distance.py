def check(string1,string2,pos,flag):
    for i in range(pos,max(len(string1),len(string2))):
        if i>=min(len(string1),len(string2)):
            return True
        else:
            if string1[i]!=string2[i]:
                if flag:
                    flag=False
                    d1=False
                    if len(string1)!=len(string2):
                        return check(string1[:i]+string1[i+1:],string2,i,flag)
                    else:
                        return check(string1[:i]+string2[i]+string1[i+1:],string2,i,flag)
                else:
                    return False
    if flag:
        return False
    else:
        return True

def isEditDistanceOne(string1, string2): 
    if abs(len(string1)-len(string2))>1:
        return False
    else:
        string1,string2=[string1,string2] if len(string1)>len(string2) else [string2,string1]
        return check(string1,string2,0,True)

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))