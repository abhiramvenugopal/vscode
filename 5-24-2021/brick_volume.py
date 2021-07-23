# You should fill this functions using the volume and calculate_price functions defined below this.
# dimensions is a list with 2 values width and height respectively
# brick_count is int representing total bricks
def calculate_total_price_of_bricks(dimensions, brick_count):
    unit_price=0.00005
    length=100
    width= 60 if dimensions[0]==-1 else dimensions[0]
    height= 40 if dimensions[1]==-1 else dimensions[1]
    return int(height*width*length*unit_price*brick_count)





### Do not change anything below this line
def volume(length=100,width=60,height=40):
	return length*width*height

def calculate_price(volume, price=0.00005):
	return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)