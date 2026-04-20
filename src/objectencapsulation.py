class Person:
  __name = "Nobody"
  
  def set_name(self, name):
    self.__name = name
  
  def get_name(self):
    return self.__name
  
p = Person()
p.set_name("Aslak")
print(p.get_name())
print(p.__name)
