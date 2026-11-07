from Animal import Animal

class Lion(Animal): 

  def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)  
        self.strength = 100  
  
  def display_info(self):
    super().display_info()             
    
  def feed(self):
    super().feed()                      
    self.health_level += 15            
    self.strength += 5
    return self

  def make_sound(self):
     print("Roar")

  

  