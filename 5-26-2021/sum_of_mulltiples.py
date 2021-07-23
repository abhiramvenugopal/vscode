# Write function with name sum_of_multiples which takes a list and integer
# It should return sum of multiple of integer given.
# You can start from here
def sum_of_multiples(numbers,mult):
    sum=0
    for i in numbers:
        if i%mult==0:
            sum+=i
    return sum

	
	
# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    mult = int(input())
    print(sum_of_multiples(numbers, mult))