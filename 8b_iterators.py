class MyRange:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __iter__(self):# returns the iterator object itself
    return self

  def next(self):
    if self.a < self.b:# returns the next item in the sequence
      value = self.a
      self.a += 1
      return value
    else:
      raise StopIteration
         
myrange = MyRange(1, 4)
print (myrange.next())
print (myrange.next())
print (myrange.next())
#print (myrange.next())

print("Using for loop")

class MyRange1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self): # returns the iterator object itself
        return self

    def __next__(self): # returns the next item in the sequence
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration
for value in MyRange1(1, 4):
     print(value)