def numbers(list):
    a = list[0]
    for i in list:
        if i > a :
            a = i
    return(a)
print(numbers([1, 2, 3, 4, 10, 7, 24,]))
        

