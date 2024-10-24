class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    if x1<x2 and y1>y2:
      self.x1 = x1
      self.y1 = y1 
      self.x2 = x2 
      self.y2 = y2 
    else:
      print("Incorrect coordinates of the rectangle!")
        
  def width(self):
    return self.x2-self.x1
      
  def height(self):
    return self.y1-self.y2
  
  def area(self):
    return self.width()*self.height()
  
  def perimeter(self):
    return 2 * self.width() + 2 * self.height()

r = Rectangle (2, 7, 8, 4)
print("Area: " + str(r.area()))
print("Perimeter: " + str(r.perimeter()))