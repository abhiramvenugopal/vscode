# def longestCon(arr,collect):
#     if len(arr)==0:
#         return
#     else:
#         count=0
#         item=arr[0]
#         temp=[]
#         for i in range(1,len(arr)):
#             if item+1==arr[i]:
#                 item=arr[i]
#                 count+=1
#             else:
#                 temp.append(arr[i])
#         collect.append(count+1)
#         longestCon(temp,collect)
        



n=int(input())
arr=[int(i) for i in input().split()]
# collect=[]
# longestCon(arr,collect)
# print(max(collect))
maxx=1
while(len(arr)!=0):
    temp=[]
    count=0
    item=arr[0]
    for i in range(1,len(arr)):
        if item+1==arr[i]:
            item=arr[i]
            count+=1
        else:
            temp.append(arr[i])
    arr=temp
    if count+1>maxx:
        maxx=count+1
print(maxx)