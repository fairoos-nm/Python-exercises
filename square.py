def table(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i*j, end= ' ')
            if j == n:
                print("\n")
            
table(5)
