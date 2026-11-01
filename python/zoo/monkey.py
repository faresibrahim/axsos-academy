from Animal import Animal

class Monkey(Animal): 
  def __init__(self, name, age, health_level, happiness_level):
          super().__init__(name, age, health_level, happiness_level)  
          self.energy = 100  

  def display_info(self):
    super().display_info()             
    print(f"Energy: {self.energy}") 
  
  def feed(self):
    super().feed()                      
    self.health_level += 15            
    self.energy += 20
    return self

  def make_sound():
      print("chatter")
