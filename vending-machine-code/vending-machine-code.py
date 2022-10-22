class Soda_Machine:
  paid = False
  balance = 0

  def eject_soda(self):
    if self.paid == False:
      print('Please insert money')
    else:
      print('Enjoy the soda!')

  def pay(self, amount):
    self.balance += amount
    
  def select_soda(self):
    if self.balance >= 1:
      self.paid = True
      self.balance -= 1
    else:
      self.paid = False