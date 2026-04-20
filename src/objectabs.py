from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
      pass

class Square(Shape):
  height = -1
  width = -1
  
  def __init__(self, height, width):
    self.height = height
    self.width = width
  
  def area(self):
    return self.height * self.width
  
s = Square(2, 3)
print(s.area())

