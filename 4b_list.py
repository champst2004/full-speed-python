def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  l1.remove(l2[0])
  l1.remove(l2[1])
  return l1

l1 = removeList()
print(l1)


def removeList1():
  
  l3 = [1, 4, 9, 10, 23]
  l4 = [4, 9]
  for elem in l4:
    l3.remove(elem)
  return l3

l3 = removeList1()
print(l3)