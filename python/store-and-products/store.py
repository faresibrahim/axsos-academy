from products import Product

class Store:
  def __init__(self, name):
    self.name=name
    self.products=[]
  

  
  def add_product(self, new_product, price, category):
    self.products.append(Product(new_product, price, category))
    return self
  
  def sell_product(self, id):
    self.products.pop(id)
    return self
  
  def inflation(self, percent_increase):
    n=len(self.products)
    for i in range(n):
      self.products[i].update_price(percent_increase, True)

  def set_clearance(self, category, percent_discount):
    for product in self.products:
      if product.category==category:
        product.update_price(percent_discount, False)

store1=Store("litchi")
store1.add_product("Ramen", 30, "Soup").add_product("Dynamite", 20, "Chicken")

store1.set_clearance("Chicken", 15)
# print(store1.products)
n=len(store1.products)
for i in range(n):
  store1.products[i].print_info()

