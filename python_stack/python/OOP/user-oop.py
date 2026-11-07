class User:

  def __init__(self, name, email):
    self.name=name
    self.email=email
    self.account_balance=0

  def make_deposit(self, amount):
    self.account_balance += amount

  def make_withdrawal(self, amount):
    self.account_balance -= amount

  def display_user_balance(self):
    print(self.account_balance)

# transfer_money method to transfer money between users
def transfer_money(user1, user2, amount):
    user1.account_balance -= amount
    user2.account_balance += amount

instance1 = User('fares', 'fares.a.ibrahim@gmail.com')
instance2 = User('elias', 'elias.ibrahim@gmail.com')
instance3 = User('mayra', 'mayra.handal@gmail.com')

instance1.make_deposit(10)
instance1.make_deposit(20)
instance1.make_deposit(30)
instance1.make_withdrawal(30)

print(instance1.account_balance)

instance2.make_deposit(50)
instance2.make_deposit(130)
instance2.make_withdrawal(40)
instance2.make_withdrawal(80)
print(instance2.account_balance)

instance3.make_deposit(290)
instance3.make_withdrawal(130)
instance3.make_withdrawal(65)
instance3.make_withdrawal(30)
print(instance3.account_balance)


transfer_money(instance1, instance3, 20)
print(instance3.account_balance)
