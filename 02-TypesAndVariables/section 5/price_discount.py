price = int(input('Enter the price: '))
discount = int(input('Enter the discount: '))

price_disc = price * discount / 100
reduction = price - price_disc

print(f"Price with discount: {price_disc}")
print(f"Reduction: {reduction}")