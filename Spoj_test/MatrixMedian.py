def matrixMedian(matrix,n,m):
    arr=[]
    for i in range(n):
        arr+=matrix[i]
    arr.sort()
    if len(arr)%2==0:
        return (arr[len(arr)//2-1]+arr[len(arr)//2-1])//2
    else:
        return arr[len(arr)//2]
for _ in range(int(input())):
    n,m=[int(i) for i in input().split()]
    matrix=[[int(i) for i in input().split()] for _ in range(n)]
    print(matrixMedian(matrix,n,m))