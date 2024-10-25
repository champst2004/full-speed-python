class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    evenArray = []
    for i in range(1, self.n+1):
      if i % 2 == 0:
        evenArray.append(i)
    return evenArray
    
myrange = MyRange(8)
print (myrange.next())