class Animal:
  alive = False

class Person (Animal):
  name = "Nobody"
  
  def __init__(self, name):
    self.name = name
    self.alive = True
  
p = Person("Aslak")
print(p.alive)

