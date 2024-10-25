class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    arr = []
    for i in range(self.n):
      if i <= 1:
        arr.append(i)
      else:
        arr.append(arr[i-2] + arr[i-1])
    return arr
  
myrange = MyRange(8)
print(myrange.next())