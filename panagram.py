def input_sen():
    """Take input from user"""
    sent = input("enter a sentence: ")
    """convert string in to list"""
    sentence = list(sent)
    return sentence

def list_of_alpha():
    """make a list of all alphabet"""
    alpha = ('abcdefghijklmnopqrstuvwxyz')
    list_is =list(alpha)
    return list_is

def panagram():
    """Check panagram or not"""
    sentence = input_sen()
    if " " in sentence:
        sentence.remove(" ")
    listed = list_of_alpha()
    for i in listed:
        list = []
        if i not in  sentence: 
            list.append(i)
    if len(list) == 0:
        return True
    else:
        return False

if panagram() == True:
    print("Nice! this is a panagram")
else:
    print("This is not a panagram")
    
            

