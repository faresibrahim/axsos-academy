class BankAccount:
  rate=0
  account_balance=0
  def __init__(self, int_rate, balance):
    self.rate=int_rate
    self.account_balance=balance
    
  
  def deposit(self, amount):
    self.account_balance += amount
    return self
  
  def withdraw(self, amount):
    self.account_balance -= amount
    return self
  
  def display_account_info(self):
    print('Balance: ', self.account_balance)
    return self
  
  def yield_interest(self):
    self.account_balance = self.account_balance*self.rate
    return self




class User:

  def __init__(self, name, email):
    self.name=name
    self.email=email
    self.bank_account=BankAccount(int_rate=2, balance=0)

  
  def display_user_balance(self):
    print(self.bank_account.account_balance)
    return self
  
# transfer_money method to transfer money between users
def transfer_money(user1, user2, amount):
    user1.bank_account.withdraw(amount)
    user2.bank_account.deposit(amount)

instance1 = User('fares', 'fares.a.ibrahim@gmail.com')
instance2 = User('elias', 'elias.ibrahim@gmail.com')
instance3 = User('mayra', 'mayra.handal@gmail.com')

instance1.bank_account.deposit(50).deposit(130).withdraw(40).withdraw(80)
print(instance1.bank_account.account_balance)



instance2.bank_account.deposit(50).deposit(130).withdraw(40).withdraw(80)
print(instance2.bank_account.account_balance)

instance3.bank_account.deposit(50).deposit(130).withdraw(40).withdraw(80)
print(instance3.bank_account.account_balance)


transfer_money(instance1, instance3, 20)
print(instance3.bank_account.account_balance)
