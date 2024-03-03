#!/usr/bin/env python3

from cash_register import CashRegister

import io
import sys

class TestCashRegister:
    '''CashRegister in cash_register.py'''

    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)

    def reset_register_totals(self):
        '''Reset the register totals'''
        self.cash_register.items.clear()
        self.cash_register_with_discount.items.clear()

    def test_discount_attribute(self):
        '''Takes one optional argument, a discount, on initialization.'''
        assert self.cash_register.discount == 0
        assert self.cash_register_with_discount.discount == 20

    def test_total_attribute(self):
        '''Sets an instance variable total to zero on initialization.'''
        assert self.cash_register.last_transaction_amount == 0
        assert self.cash_register_with_discount.last_transaction_amount == 0

    def test_items_attribute(self):
        '''Sets an instance variable items to empty list on initialization.'''
        assert self.cash_register.items == []
        assert self.cash_register_with_discount.items == []

    def test_add_item(self):
        '''Accepts a title and a price and increases the total.'''
        self.cash_register.add_item("eggs", 0.98)
        assert self.cash_register.last_transaction_amount == 0.98
        self.reset_register_totals()

    def test_add_item_optional_quantity(self):
        '''Also accepts an optional quantity.'''
        self.cash_register.add_item("book", 5.00, 3)
        assert self.cash_register.last_transaction_amount == 15.98
        self.reset_register_totals()

    def test_add_item_with_multiple_items(self):
        '''Doesn't forget about the previous total.'''
        self.cash_register.add_item("Lucky Charms", 4.5)
        assert self.cash_register.last_transaction_amount == 20.48
        self.cash_register.add_item("Ritz Crackers", 5.0)
        assert self.cash_register.last_transaction_amount == 25.48
        self.cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
        assert self.cash_register.last_transaction_amount == 30.48
        self.reset_register_totals()

    def test_apply_discount(self):
        '''Applies the discount to the total price.'''
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        assert self.cash_register_with_discount.last_transaction_amount == 800
        ##self.reset_register_totals()

    def test_apply_discount_success_message(self):
        '''Prints success message with updated total.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "After the discount, the total comes to $1000.00.\n"
        self.reset_register_totals()

    def test_apply_discount_when_no_discount(self):
        '''Prints a string error message that there is no discount to apply.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register.apply_discount()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "There is no discount to apply.\n"
        self.reset_register_totals()

    def test_items_list_without_multiples(self):
        '''Returns an array containing all items that have been added.'''
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99)
        new_register.add_item("tomato", 1.76)
        assert new_register.items == ["eggs", "tomato"]

    def test_items_list_with_multiples(self):
        '''Returns an array containing all items that have been added, including multiples.'''
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99, 2)
        new_register.add_item("tomato", 1.76, 3)
        assert new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"]

    def test_void_last_transaction(self):
        '''Subtracts the last item from the total.'''
        self.cash_register.add_item("apple", 0.99)
        self.cash_register.add_item("tomato", 1.76)
        self.cash_register.void_last_transaction()
        assert self.cash_register.last_transaction_amount == 0.99
        self.reset_register_totals()

    def test_void_last_transaction_with_multiples(self):
        '''Returns the total to 0.0 if all items have been removed.'''
        self.cash_register.add_item("tomato", 1.76, 2)
        self.cash_register.void_last_transaction()
        assert self.cash_register.last_transaction_amount == 0.0
        self.reset_register_totals()
