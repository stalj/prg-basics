price = float(input("Enter price: "))
discount = 0.01*int(input("Enter discount %: "))
price_discount=price*(1-discount)
Reduction=price-price_discount
print(f"Price with discount: {round(price_discount,2)}")
print(f"Reduction: {round(Reduction,2)}")