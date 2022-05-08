def join(s,iterable):
    new_str = ""
    counter = 1
    for word in iterable:
        if counter != len(iterable):
            new_str += word + s
            counter += 1
        else:
            new_str += word
    return new_str

print(join('###',['hello','world']))
print(join("Test", {"name": "John", "country": "Norway"}))
