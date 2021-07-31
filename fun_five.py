def funfive(n):
    count=0
    while n%5==0:
        count+=1
        n=n/5
    return count
for _ in range(int(input())):
    n=int(input())
    i=1
    summ=0
    while(summ<n):
        summ+=funfive(i)
        i+=1
    print(i-1)





    
n = int(input())
 
cost_by_car = list(map(int, input().split()))
cost_by_bus = list(map(int, input().split()))
 
ans = 0
 
cost_for_changing_to_car = []
cost_for_changing_to_bus = []
 
for i in range(n):
    if cost_by_car[i] <= cost_by_bus[i]:
        ans += cost_by_car[i]
        cost_for_changing_to_bus.append(cost_by_bus[i] - cost_by_car[i])
    else:
        ans += cost_by_bus[i]
        cost_for_changing_to_car.append(cost_by_car[i] - cost_by_bus[i])
        
cost_for_changing_to_car = sorted(cost_for_changing_to_car)
cost_for_changing_to_bus = sorted(cost_for_changing_to_bus)
 
diff = len(cost_for_changing_to_car) - len(cost_for_changing_to_bus)
 
if abs(diff) > 1:
    for i in range(abs(diff)//2):
        if diff > 1:
            ans += cost_for_changing_to_car[i]
        else:
            ans += cost_for_changing_to_bus[i]
 
print(ans)