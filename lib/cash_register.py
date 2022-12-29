#!/usr/bin/env python3
import ipdb

class CashRegister:
  pass
  def __init__( self, discount = 0 ):
    self.discount = discount
    self.total = 0
    self.items = []
    self.item_list = []

  def add_item( self, title, price, quantity = 1 ):
    self.total += price * quantity
    self.item_list.append( { 'name': title, 'price': price, 'quantity': quantity } )
    for item in range( quantity ):
      self.items.append( title )

  def apply_discount( self, ):
    if self.discount:
      total = self.total
      self.total = total - ( total * ( self.discount / 100 ) )
      print( f"After the discount, the total comes to $%.0f." % self.total )
    else: print( "There is no discount to apply." )

  def void_last_transaction( self ):
      self.total -= self.item_list[-1]['price'] * self.item_list[-1]['quantity']
      for x in range( self.item_list[-1]['quantity'] ):
        self.items.pop()
      self.item_list.pop()
      if not self.items and not self.item_list :
        self.total = 0.0
    # ipdb.set_trace()