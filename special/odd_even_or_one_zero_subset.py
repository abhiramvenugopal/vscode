# You are given an array A of N positive integer values. A subarray of this array is called Odd-Even subarray if the number of odd integers in this subarray is equal to the number of even integers in this subarray.

# Find the number of Odd-Even subarrays for the given array.

# Input
# The input consists of two lines.

# First line denotes N - size of array.

# Second line contains N space separated positive integers denoting the elements of array A.

# Output
# Print a single integer, denoting the number of Odd-Even subarrays for the given array.

# Example
# Input:

# 4

# 1 2 1 2

# Output:

# 4

# also we can do this prokgrame can use for zero one case also




def countOddEvenSubArray(arr,n):
    dict={}
    count=0
    sum=0
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=-1
        else:
            arr[i]=1
        sum+=arr[i]
        if sum==0:
            count+=1
        if sum in dict:
            count+=dict[sum]
        dict[sum]=dict.get(sum,0)+1
    print(count)
n=int(input())
arr=[int(i) for i in input().split()]
countOddEvenSubArray(arr,n)

