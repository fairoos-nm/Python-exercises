
def evaluate(s):
    list = []
    for i in s:
        if  i.isdigit():
            list.append(i)

        else:
            x = int(list.pop())
            y = int(list.pop())

            if i == "+":
                ans = x + y
  
            elif i == "-":
                ans = x - y
            list.append(ans)

            elif i == "*":
                ans = x * y
            list.append(ans)

            elif i == "/":
                ans = x / y
            list.append(ans)

            
    return (list.pop())

print(evaluate("23+5+"))       
