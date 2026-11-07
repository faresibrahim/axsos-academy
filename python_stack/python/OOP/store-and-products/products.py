class Product:
  def __init__(self, name, price, category):
    self.name=name
    self.price=price
    self.category=category

  def update_price(self, percent_change, is_increased):
    amount=self.price*(percent_change/100)
    if is_increased==True:
      self.price += amount
    else:
      self.price -= amount
  def print_info(self):
    print(self.name)
    print(self.price)
    print(self.category)



