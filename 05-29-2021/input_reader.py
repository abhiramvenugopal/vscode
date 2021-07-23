class ReadInput:
    def __init__(self,n) :
        self.n=n
        self.num_list=[]
    def read_strings(self):
        for _ in range(self.n):
            self.num_list.append(input())
    def read_integers(self):
        for _ in range(self.n):
            self.num_list.append(int(input()))
    def read_floats(self):
        for _ in range(self.n):
            self.num_list.append(round(float(input()),2))
    
n=int(input())
category=input()
obj=ReadInput(n)
if category=="integer":
    obj.read_integers()
elif category=="string":
    obj.read_strings()
elif category=="float":
    obj.read_floats()

for i in range(obj.n):
    print(i,obj.num_list[i])