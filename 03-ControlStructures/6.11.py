product_amount=int(input('Number of products purchased: '))
product_price=float(input('Product price: '))
pay=0
if product_amount>=1:
    pay +=product_price
if product_amount>=2:
    pay +=product_price
while product_amount>2:
    pay +=product_price*0.75
    product_amount-=1
print(f'Amount to pay: {pay}')
