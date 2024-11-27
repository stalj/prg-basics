my_tuple = (50, 30, 40, 50, 30, 50)
value = 50
counter = 0

for val in my_tuple:
    if val == value:
        counter += 1

print()
print('Tuple: ', my_tuple)
print('Value: ', value)
print('Number of occurrences', counter)