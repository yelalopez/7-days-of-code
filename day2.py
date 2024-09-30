stock_updated = { 'notebook' : 5, 
         'pencil' : 10,
          'pen' : 20,
          'eraser' : 8, 
          'ruler' : 5, 
          'highlighter' : 4, 
          'glue stick' : 5, 
          'paper clip' : 3, 
          'stapler' : 5, 
          'scissors': 4 }

check_product = input('Which product do you want to check?: ').lower()

if check_product in stock_updated:
  print(f'The {check_product} is in stock')
else:
  print(f'O {check_product} not in stock')


product_sold = input('Product: ').lower()
quantity = int(input('Quantity: '))

if product_sold in stock_updated:
  stock_updated[product_sold] -= quantity
  print(f'Updated stock: {product_sold.capitalize()} = {stock_updated[product_sold]}')
else:
  print(f'{stock_updated[product_sold]} not avaliable')

