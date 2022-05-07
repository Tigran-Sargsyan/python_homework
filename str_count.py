def count(s,value,start=0,end=0):
    length = len(value)
    counter = 0
    if end == 0:
        end = len(s)
    s = s[start:end]
    for i in range(len(s)-length):
        if s[i:i+length] == value:
            counter += 1
    return counter

print(count("hello world",'ll'))            
print(count("dimension reduction",'e',2))
print(count("dimension reduction",'e',5))
