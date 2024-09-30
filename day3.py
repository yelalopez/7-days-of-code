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


for product, quantity in stock_updated.items():
 print(f'{product.capitalize()} = {quantity}')



while True:
  product_sold = input('Enter product or type exit: ').lower().strip()
  
  if product_sold == 'exit':
    break
  
  if product_sold in stock_updated:
    quantity = int(input('Quantity: '))

    if quantity <= stock_updated[product_sold]:
      stock_updated[product_sold] -= quantity
      print(f'Updated stock: {product_sold.capitalize()} = {stock_updated[product_sold]}')

      if stock_updated[product_sold] == 0:
        print(f'{product_sold} is now out of stock!') 
  
    else:
      print(f'{product_sold} not enough stock. Avaliable {stock_updated[product_sold]} units')

  else:
    print(f'{product_sold} is not in stock. Please choose a valid product')
  