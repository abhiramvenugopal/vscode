# You should name your function as difference_sum_even_odd_index
# It should take a list of integers
# Return an integer
def difference_sum_even_odd_index(numbers):
    sum_odd=0
    sum_even=0
    for i in numbers:
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    return sum_even-sum_odd
    


# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))