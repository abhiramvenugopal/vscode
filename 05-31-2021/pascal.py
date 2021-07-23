def pascal(n):
    print(1)
    num_list=[1,1]
    for _ in range(n-1):
       
        for i in num_list:
            print(i,end=" ")
        print()
        temp_list=[]
        temp_list.append(1)
        for i in range(1,len(num_list)):
            temp_list.append(num_list[i-1]+num_list[i])
        temp_list.append(1)
        num_list=temp_list
        
n=int(input())
pascal(n)


