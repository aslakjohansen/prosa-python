class Person:
  name = "Nobody"
  
  def __init__(self, name):
    self.name = name
  
  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name
  
p = Person("Aslak")
print(p.get_name())

