def findMinCountCoffeeMachine(arr,n):
    dict={}
    for a in arr:
        time=str(a[0])+":"+str(a[1])
        dict[time]=dict.get(time,0)+1
    return dict[max(dict,key=dict.get)]

for _ in range(int(input())):
    n=int(input())
    arr=[[int(i) for i in input().split()] for _ in range(n)]
    print(findMinCountCoffeeMachine(arr,n))
