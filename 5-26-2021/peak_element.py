def peak(num_list):
    for i in range(n):
        if (i==0 and num_list[i]>num_list[i+1]) or  (i==n-1 and num_list[i]>num_list[i-1])or (num_list[i-1]<num_list[i] and num_list[i]>num_list[i+1])  :
            return i+1
    return -1

t=int(input())
for _ in range(t):
    n=int(input())
    num_list=[i for i in input().split()]
    print(peak(num_list))
