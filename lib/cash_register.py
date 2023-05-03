#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.prev_transaction = 0

    def add_item(self, title, price, quantity = 1):
      self.title = title
      self.quantity = quantity
      newTotal = price*quantity
      self.total += newTotal
      self.prev_transaction = newTotal
      for n in range(quantity):
        self.items.append(title)
    
    def apply_discount(self):
      if self.discount > 0:
        self.total -= int((self.discount/100) * self.total)
        print(f"After the discount, the total comes to ${self.total}.")
      else:
        print("There is no discount to apply.")
    
    def CashRegister(self):
      return(self.list)

    def void_last_transaction(self):
      self.total -= self.prev_transaction
      pass
