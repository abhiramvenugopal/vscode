# Write a function with name even_odd_separator, you should exactly the same name
# This even_odd_separator functions should take a list of integers and return a list
# you can start from here	
def even_odd_separator(numbers):
    odd_list=[]
    even_list=[]
    for i in numbers:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)	
    return odd_list+even_list

### Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
    	print(num)