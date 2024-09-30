stock = {}

def add_product(product, quantity):
  if product in stock:
    stock[product] += quantity
    print(f'{product} = {stock[product]}')
  
  else:
    stock[product] = quantity
    print(f'{product} = {stock[product]}')

def remove_produt(product):
  if product in stock:
    del stock[product]
    print(f'{product} removed from stock')
  else:
    print(f'{product} not in stock')
  

add_product('pen', 5)
remove_produt('pencil')