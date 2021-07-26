def zeroSum(matrix, rows, cols):
    transpose=[[0]*rows for _ in range(cols)]
    count=0
    for i in range(rows):
        summ=0
        for j in range(cols):
            summ+=matrix[i][j]
            transpose[j][i]=matrix[i][j]
        if summ==0:
            count+=1
    for i in transpose:
        if sum(i)==0:
            count+=1
    return count
        





for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))