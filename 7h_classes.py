class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1 
    self.y1 = y1 
    self.x2 = x2 
    self.y2 = y2 
        
  def width(self):
    return self.x2 - self.x1
      
  def height(self):
    return self.y2 - self.y1
  
  def area(self):
    return self.width() * self.height()

class Square(Rectangle):
  def __init__(self, x1, y1, length):
    x2 = x1 + length
    y2 = y1 + length
    super().__init__(x1, y1, x2, y2)
    
square = Square (2, 7, 7)
print("Length: " + str(square.width()) + ", Area: " + str(square.area()))
square2 = Square (1, 3, 5)
print("Length: " + str(square2.width()) + ", Area: " + str(square2.area()))