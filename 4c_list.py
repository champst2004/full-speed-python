print([x**2 for x in [0, 1, 2, 3]])
print([x**2 for x in range(4)])
print([x**2 for x in range(1, 11) if x % 2 == 0])
print([x**2 for x in range(1, 11, 2)])

l1 = [x for x in range(0, 21) if (x % 2 == 0)]
l2 = [x for x in range(0, 21) if (x not in l1)]