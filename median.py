def numbers(list):
    count = 0
    mode_val = 0
    position = 0
    for i in list:
        count = count + 1
    position = count / 2
    mode_val = count % 2
    if mode_val != 0:
        print(list[position])
        
    else:
        print(list[position], list[position - 1])
numbers([1, 2, 3, 4, 5, 6, 7, 8])    
