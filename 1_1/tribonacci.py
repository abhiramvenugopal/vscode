# def tribonacci(n):
#     if n<=2:
#         return 0
#     elif n==3:
#         return 1
#     else:
#         return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

# print(tribonacci(int(input())))


def tribonacci(n):
    arr=[0,0,1]
    if n<=3:
        return arr[n-1]
    else:
        for i in range(3,n):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        return arr[-1]

print(tribonacci(int(input())))


