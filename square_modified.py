def table(n):
    for i in range(1,n+1):
        if i ==2:
            print ('-' * (n * 2))
        for j in range(1,n+1):
            print(i*j, end= ' ')
            if j == 1:
                print('|', end = '')
            if j == n:
                print("\n")
            
table(5)
