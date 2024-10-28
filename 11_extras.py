strings = ["hi", "hello", "my", "world"]

lengths = map(len, strings)

print(list(lengths))

def nice(string):
    return len(string) > 2

filtered = filter(nice, strings)

print(list(filtered))