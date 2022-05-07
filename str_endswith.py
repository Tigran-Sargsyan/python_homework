def endswith(s,value,start=0,end=0):
    if end == 0:
        end = len(s)
    s = s[start:end]
    if len(value)>len(s):
        return False
    else:
        for i in range(-1,len(value)+1,-1):
            if value[i] != s[i]:
                return False
        return True

print(endswith("hello","llo"))
print(endswith("heyyy","yyy",3,5))
print(endswith("heyy","yy",))
