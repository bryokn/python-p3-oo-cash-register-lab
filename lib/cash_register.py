#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.last_transaction_amount = 0
        self.discount = discount

    def add_item(self, item_name, price_per_item, quantity=1):
      total_price = price_per_item * quantity
      self.items.extend([item_name] * quantity)
      self.total += total_price
      self.last_transaction_amount += total_price  

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.last_transaction_amount, 2)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            price_per_item = self.items.pop()
            self.total -= price_per_item

    def get_total_price(self):
        return sum(price for price in self.items)

    def update_last_transaction_amount(self):
        if self.items:
            self.last_transaction_amount = sum(price for price in self.items)
        else:
            self.last_transaction_amount = 0
