def game(arr):
    # print(arr)
    arr.sort()
    totalTurns=arr[1]
    # print(totalTurns,"mid")
    if (arr[2]-arr[1])%2==1:
        totalTurns+=1
    totalTurns+=(arr[2]-arr[1])//2
    print(totalTurns)
for _ in range(int(input())):
    arr=[int(i) for i in input().split()]
    game(arr)