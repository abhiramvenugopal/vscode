# Swap K
# Given an array Arr of size N, swap the K-th element from beginning with K-th element from end.

# Constraints:
# 1 <= K <= N
# Input
# First line contains two space seperated integers, denoting N and K respectively. The next line contains N space seperated values, denoting the elements of the array Arr.

# Output
# N space seperated values, denoting the elements of the resultant array.

# Example
# Input1:

# 8 3
# 1 2 3 4 5 6 7 8
# Output1:

# 1 2 6 4 5 3 7 8
# Explanation:

# Kth element from beginning is 3 and from end is 6.



n,k=map(int,input().split())
num_list=list(map(int,input().split()))
temp=num_list[k-1]
num_list[k-1]=num_list[n-k]
num_list[n-k]=temp
for i in num_list:
    print(i,end=" ")