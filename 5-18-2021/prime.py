
# Find if given number is prime
# Find if the given integer is prime number.

# Input
# FirstLine contains an interger specifying no. of test cases. Each line contains integers specifying value of number in each test case.

# Output
# Yes if number is prime. No is not for each testcase.

# Example
# Input: 3

# 2

# 4

# 5

# Output: Yes

# No

# Yes



# ----------------------------------------------------------------------------------


n=int(input())
num_list=[]
for i in range(n):
    num_list.append(int(input()))
for val in num_list:
    count=0
    if val<=0:
        print("No")
    else:
        for i in range(1,val):
            if val%i==0:
                count+=1
            if count>1:
                break
        if count>1:
            print("No")
        else:
            print("Yes")