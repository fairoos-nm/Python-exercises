def numbers(list):
    """find smallet number from list"""
    a = list[0]
    for i in list:
        """Take each element from list one by one"""
        if i < a:
            """Check the smallest element"""
            a = i
    return a
print(numbers([-1, 0, 3, -5, 7]))
