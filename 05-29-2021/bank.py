class Bank:
    def __init__(self):
        self.balance=0
    def credit(self,amount):
        self.balance+=amount
    def debit(self,amount):
        self.balance+=amount
n=int(input())
b=Bank()
for _ in range(n):
    val=int(input())
    if val<0:
        b.debit(val)
    else:
        b.credit(val)
print(b.balance)
