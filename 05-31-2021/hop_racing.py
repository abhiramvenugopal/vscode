class HopRacing:
    def __init__(self):
        self.no_of_rounds=0
    def getRounds(self,l1):
        no_hope=0
        for i in l1:
            self.no_of_rounds+=1
            no_hope+=i
            if(no_hope>=10):
                break
                
           
    
n=int(input())
l1=[]
l2=[]
for _ in range(n):
    index,val=map(int,input().split())
    if index==1:
        l1.append(val)
    if index==2:
        l2.append(val)
hp1=HopRacing()
hp2=HopRacing()
hp1.getRounds(l1)
hp2.getRounds(l2)
if (hp1.no_of_rounds==hp2.no_of_rounds):
    print(-1)
elif(hp1.no_of_rounds<hp2.no_of_rounds):
    print(1)
else:
    print(2)