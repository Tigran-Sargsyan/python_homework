def rfind(s,value,start=0,end=0):
    if end == 0:
        end = len(s)
    s = s[start:end]
    print(s)
    length = len(value) - 1 
    for i in range(len(s)-1,-1,-1): #Looping backwards
        if s[i-length:i+1] == value:
            return i-length+start
    return -1

print(rfind("This is a sentence!!!","enc"))
print(rfind("This is a sentence!","te",3,15))
print(rfind("Hello, welcome to my world.","e", 5, 10))
