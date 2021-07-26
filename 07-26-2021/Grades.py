for _ in range(int(input())):
    n=int(input())
    roundedVal=(((n//5)+1)*5)
    if n<38:
        print(n)
    elif roundedVal-n < 3:
        print(roundedVal)
    else:
        print(n)