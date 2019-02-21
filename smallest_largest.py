def numbers(list):
    a = list[0]
    b = 0
    for i in list:
        if i > a:
            a = i 
        
        else:
            b = i
            
    return(a,b)
print("largest and smallest numbers in this list are: ",numbers([1, 2, 5, -1, 7]))

