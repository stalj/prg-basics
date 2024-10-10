import pandas as pd

# Tworzenie danych do sklepu odzieżowego
data = {
    'Product ID': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'Product Name': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Cap', 'Scarf', 'Belt', 'Socks', 'Sweater', 'Shorts'],
    'Category': ['Tops', 'Bottoms', 'Outerwear', 'Footwear', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Tops', 'Bottoms'],
    'Price': [19.99, 49.99, 89.99, 59.99, 15.99, 9.99, 14.99, 4.99, 39.99, 24.99],
    'Stock Quantity': [50, 40, 30, 20, 60, 80, 70, 100, 35, 45]
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Zapis do pliku CSV
csv_file_path = '/mnt/data/clothing_store_products.csv'
df.to_csv(csv_file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Clothing Store Products", dataframe=df)
