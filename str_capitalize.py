def capitalize(s):
    big_s = ""
    if "a" <= s[0] <= "z":
        big_s += chr(ord(s[0]) - 32)
    else:
        big_s += s[0]

    for i in s[1:]:
        if "A" <= i <= "Z":
            big_s += chr(ord(i) + 32)
        else:
            big_s += i

    return big_s

print(capitalize("heY"))
print(capitalize("hello WoRLd"))                                                          
