# n = int(input())
 
# cost_by_car = list(map(int, input().split()))
# cost_by_bus = list(map(int, input().split()))
 
# ans = 0
 
# cost_for_changing_to_car = []
# cost_for_changing_to_bus = []
 
# for i in range(n):
#     if cost_by_car[i] <= cost_by_bus[i]:
#         ans += cost_by_car[i]
#         cost_for_changing_to_bus.append(cost_by_bus[i] - cost_by_car[i])
#     else:
#         ans += cost_by_bus[i]
#         cost_for_changing_to_car.append(cost_by_car[i] - cost_by_bus[i])
        
# cost_for_changing_to_car = sorted(cost_for_changing_to_car)
# cost_for_changing_to_bus = sorted(cost_for_changing_to_bus)
 
# diff = len(cost_for_changing_to_car) - len(cost_for_changing_to_bus)
 
# if abs(diff) > 1:
#     for i in range(abs(diff)//2):
#         if diff > 1:
#             ans += cost_for_changing_to_car[i]
#         else:
#             ans += cost_for_changing_to_bus[i]
 
# print(ans)


n=int(input())
car=[int(i) for i in input().split()]
bus=[int(i) for i in input().split()]
carChange=[]
busChange=[]
res=0
for i in range(n):
    if car[i]<=bus[i]:
        res+=car[i]
        busChange.append(bus[i]-car[i])
    else:
        res+=bus[i]
        carChange.append(car[i]-bus[i])
carChange.sort()
busChange.sort()
diff=len(carChange)-len(busChange)

if abs(diff)>1:
    for i in range(abs(diff)//2):
        if diff>1:
            res+=carChange[i]
        else:
            res+=busChange[i]
print(res)