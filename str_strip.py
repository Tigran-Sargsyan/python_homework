def strip(s,delete_set="' '"):
    start,end = 0,len(s)
    for i in s:
        if i not in delete_set:
            break
        start += 1
    
    for i in s[::-1]:
        if i not in delete_set:
            break
        end -= 1

    return s[start:end]

print(strip("This is a sentence  "),end=",")
print(strip(" hello world  "),end=",")
print(strip(",,,,,rrttgg.....banana....rrr",",.grt"))                     
