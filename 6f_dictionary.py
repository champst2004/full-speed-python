from collections import defaultdict
from collections import Counter

def get_counter(s):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    print(counter)

get_counter("aba")

def get_counter2(s):
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    print(counter)

get_counter2("aba")

def get_counter3(s):
    counter = Counter(s)
    print(counter)

get_counter3("aba")