n,k=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
charged=int(input())
actual=sum(arr[:k]+arr[k+1:])//2
if actual==charged:
    print("It is Correct!")
else:
    print(charged-actual)