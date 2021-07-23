# Your class should be named `Circle`.
# Method to get area should be named `getArea`
# Method to get circumference should be named `getCircumference`.
# Your class should take radius `r` as input when creating an object.
class Circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
        if self.r<0:
            self.r=0
    def getArea(self):
        return Circle.pi*(self.r**2)
    def getCircumference(self):
        return 2*Circle.pi*self.r  
if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))