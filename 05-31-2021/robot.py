class Robot:
    def __init__(self) -> None:
        self.location=[0,0]
    def moveUp(self):
        self.location[1]+=1
    def moveDown(self):
        self.location[1]-=1
    def moveRight(self):
        self.location[0]+=1
    def moveLeft(self):
        self.location[0]-=1

m=int(input())
rb=Robot()
for _ in range(m):
    cmd=input()
    if cmd=="up":
        rb.moveUp()
    elif cmd=="down":
        rb.moveDown()
    elif cmd=="right":
        rb.moveRight()
    elif cmd=="left":
        rb.moveLeft()
print(rb.location[0])
print(rb.location[1])

