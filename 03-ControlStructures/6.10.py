current_price=float(input('Current product price: '))
previous_price=float(input('Previous product price: '))
reduction_in_price=(previous_price-current_price)/previous_price
if reduction_in_price>0.10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction_in_price*100}%")