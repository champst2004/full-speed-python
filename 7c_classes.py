class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    if x1 < x2 and y1 > y2:
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2
    else:
      print("Incorrect coordinates of the rectangle!")
        
  def __str__(self):
    return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+str(self.y2))

r = Rectangle (2, 7, 8, 4)
print(r)

'''
python has a built-in method __str__ used for the string representation of an object.
__repr__ is another built-in method which is similar to __str__. 
Both of them can be overridden for any class and there are only minor differences.

str():
makes the object readable
generates output for end-user

repr():
needs code that reproduces the object
generates output for developer

If both methods are defined in a class, __str__ is used.
In the previous exercise, you had to implement the __str__ method in the Rectangle class;
therefore, when you print one of the objects using the print() command, it prints the coordinates as x1, y1, x2, y2.
'''