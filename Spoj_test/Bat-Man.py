def rotateArray(arr,n,r):
    r=r%n
    temp=[0]*n
    if r>0:
        for i in range(n):
            temp[i-r]=arr[i]
        arr=temp
    return arr
for _ in range(int(input())):
    n,r=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    print(*(rotateArray(arr,n,r)))
