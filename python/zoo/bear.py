from Animal import Animal

class Bear(Animal): 
  def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)  
        self.fatigue = 100  

  def display_info(self):
    super().display_info()             
    print(f"Fatigue: {self.fatigue}") 
  
  def feed(self):
    super().feed()                      
    self.health_level += 15            
    self.fatigue -= 20
    return self

  def make_sound():
     print("Growl")

  
  