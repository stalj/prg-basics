product_price_before = 120
product_price_after = 100
price_reduced = 100 - (product_price_after * 100/product_price_before)

if price_reduced >= 10 and product_price_after < product_price_before:
    print(f"price before: {product_price_before}$    ->     price after: {product_price_after}$")
    print("buy this product!")
    print(f"{price_reduced:.2f}% discount!")
else:
    print(f"{product_price_before}$         ->            {product_price_after}$")
    print("no discount")