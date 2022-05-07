def find(s,value,start=0,end=0):
    if end == 0:
        end = len(s)
    s = s[start:end]
    length = len(value)
    for i in range(len(s)-length+1):
        if s[i:i+length] == value:
            return i+start
    return -1

print(find("This is a sentence!","i"))
print(find("This is a sentence!","is",3,10))
