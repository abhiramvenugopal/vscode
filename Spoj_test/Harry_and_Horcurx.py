def countOddEvenSubArray(arr,n):
    dict={}
    count=0
    sum=0
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=-1
        else:
            arr[i]=1
        sum+=arr[i]
        if sum==0:
            count+=1
        if sum in dict:
            count+=dict[sum]
        dict[sum]=dict.get(sum,0)+1
    print(count)
n=int(input())
arr=[int(i) for i in input().split()]
countOddEvenSubArray(arr,n)

