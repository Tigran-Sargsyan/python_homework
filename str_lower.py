def lower(s):
    if isinstance(s,str):
        low_s = ""
        for i in s:
            if "A"<=i<="a":
                low_s+=chr(ord(i)+32)
            else:
                low_s+=i
        return low_s
    else:
        print("The parameter is not string!")

print(lower("HeLLo WorLD"))
print(lower("MyComPUtEr"))
