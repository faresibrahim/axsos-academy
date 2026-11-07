from abc import ABC, abstractmethod

class Animal(ABC):

  def __init__(self, name, age, health_level, happiness_level):
    self.name=name
    self.age=age
    self.health_level=health_level
    self.happiness_level=happiness_level

  
  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Health level: {self.health_level}")
    print(f"Happiness level: {self.happiness_level}")
  

  def feed(self):
    self.health_level += 10
    self.happiness_level += 10
    return self

  @abstractmethod
  def make_sound(self):
    pass
  
