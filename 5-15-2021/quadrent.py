xarray=[]
for i in range(int(input())):
    xarray.append(list(map(int,input().split())))
for i in xarray:
    x=i[0]
    y=i[1]
    if x > 0 and y > 0:
        print("Q1")
    if x < 0 and y > 0:
        print("Q2")
    if x < 0 and y < 0:
        print("Q3")
    if x > 0 and y < 0:
        print("Q4")