def numbers(list):
    count = 0
    sum = 0
    for i in list:
        sum = i + sum
        count = count + 1
    mean = sum / count
    return mean
print(numbers([1, 2, 3, 5, 10]))
