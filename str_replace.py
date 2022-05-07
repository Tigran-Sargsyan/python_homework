def replace(s,old,new,counter=0):
    if counter == 0:
        counter = s.count(old)  
    new_str = ""
    length_of_old = len(old)
    i = 0
    while i < len(s):
        if s[i:i+length_of_old] == old:
            new_str += new
            counter -= 1
            i += length_of_old
            if counter == 0:
                new_str += s[i + length_of_old - 1:]
                break
        else:
            new_str += s[i]
            i += 1

    return new_str    

print(replace("hello world","l","L"))
print(replace("hello world","l","L",2))
print(replace("This is a sentence!","i","I",1))
print(replace("This is a sentence!","e","E",))
