from lion import Lion
from bear import Bear
from monkey import Monkey

class Zoo:
  def __init__(self, zoo_name):
    self.name=zoo_name
    self.animals=[]

  def add_animal(self, animal):
    self.animals.append(animal)
    return self

  def feed_animal(self, animal):
    animal.feed()
    return self

  def print_all_info(self):
    
    print("-"*30, self.name, "-"*30)
    for animal in self.animals:
      animal.display_info()


nala = Lion("Nala", 8, 100, 30)
fluf=Bear("Fluf", 6, 95, 50)
corky=Monkey("Corky", 10, 87, 50)
zoo1=Zoo("Fares's Zoo")
zoo1.add_animal(nala).add_animal(fluf).add_animal(corky)
zoo1.feed_animal(corky)
zoo1.print_all_info()

