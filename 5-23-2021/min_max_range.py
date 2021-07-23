## This function should return single integer. The integer should be maximum value of input list
## Please fill the following function
def maximum_value(input_numbers):
	return max(input_numbers)


## This function should return single integer. 
## The integer should be minimum value of input list
def minimum_value(input_numbers):
    return min(input_numbers)


## This function should return list of integer which lies between m1 and m2. 
## if m1 <= m2 return list off numbers between m1 and m2
## if m2 <= m1 return list off numbers between m2 and m1
def get_numbers_in_range(input_numbers, m1, m2):
    # Please write below this line
    ret_list=[]
    if m1 <= m2:
        ret_list=[i for i in input_numbers if i>=m1 and i<=m2]
    if m2 <= m1:
        ret_list=[i for i in input_numbers if i>=m2 and i<=m1]
    if len(ret_list)==0:
        return [-1]
    else:
        return ret_list




### Please do not change anything below this line.
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]