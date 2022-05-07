def startswith(s,value,start=0,end=0):
    if end == 0:
        end = len(s)

    s = s[start:end]        
    if len(value) > len(s):
        return False
    else:
        for i in range(len(value)):
            if value[i] != s[i]:
                return False
        return True            

print(startswith("hello","hEl"))
print(startswith("hello world","hello",0))
print(startswith("Hello world","llo",2,5))        
