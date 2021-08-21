arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphacount=97
dict={}
for i in arr:
    dict[chr(alphacount)]=i
    alphacount+=1
for _ in range(int(input())):
    res=set()
    inputArr=[i for i in input().split()]
    for s in inputArr:
        encodedStr=""
        for c in s:
            encodedStr+=dict[c]
        res.add(encodedStr)
    print(len(res))
        
