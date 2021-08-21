def checkSymetric(matrix,n):
    s={}
    for i in range(((n-1)//2)+1):
        for j in range(((n-1)//2)+1):
            if matrix[i][j]==1:
                s[(i,j)]="item"
                s[(n-1-i,j)]="item"
                s[(i,n-1-j)]="item"
                s[(n-1-i,n-1-j)]="item"
    for i in range(n):
        for j in range(n):
            if (matrix[i][j]==0 and (i,j) in s) or (matrix[i][j]==1 and (i,j) not in s):
                return "NO"
    return "YES"
for _ in range(int(input())):
    n=int(input())
    matrix=[[int(i) for i in list(input())] for _ in range(n)]
    print(checkSymetric(matrix,n))
