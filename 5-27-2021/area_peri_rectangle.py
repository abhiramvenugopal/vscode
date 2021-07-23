# Your class should be named as `Rectangle`. 
# Method to get area should be named as `rectangle_area`.
# Method to get perimeter should be named as `rectangle_perimeter`.
# You should be taking `length` and `width` as inputs when creating the object for your class.
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        self.l,self.w=[self.l,self.w] if self.l>0 and self.w>0 else[0,0]
    def rectangle_area(self):
        return self.l*self.w
    def rectangle_perimeter(self):
        return 2*self.l+2*self.w
if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())