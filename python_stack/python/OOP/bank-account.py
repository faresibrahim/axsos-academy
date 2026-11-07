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
  
account1=BankAccount(3, 300)
account2=BankAccount(2, 200)
account1.deposit(10).deposit(20).deposit(30).withdraw(50).yield_interest().display_account_info()
account2.deposit(40).deposit(50).withdraw(20).withdraw(55).withdraw(5).withdraw(15).yield_interest().display_account_info()