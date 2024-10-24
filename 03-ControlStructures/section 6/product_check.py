products = int(input("Number of products purchased: "))
product_price = 40
price = product_price * products
if products > 2:
    discount = 0.25
    price -= (products - 2) * product_price * discount

print()
print(f"Number of products purchased: {products}")
print(f"Product price: {product_price}")
print(f"Amount to pay: {price:.2f}")