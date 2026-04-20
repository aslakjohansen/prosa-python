class Person:
  name = "Nobody"
  
  def set_name(self, name):
    self.name = name
  
  def get_name(self):
    return self.name
  
p = Person()
p.set_name("Aslak")
print(p.get_name())
