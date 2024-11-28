arr = [
    [4, 5, 3, 5, 9],
    [9, 0, 1, 7, 5],
    [7, 2, 3, 0, 1]
]

print('Before: ')
for row in arr:
    print(row)

arr[0], arr[2] = arr[2], arr[0]

print('After swapping rows: ')
for row in arr:
    print(row)

arr = [
    [4, 5, 3, 5, 9],
    [9, 0, 1, 7, 5],
    [7, 2, 3, 0, 1]
]

print('Before: ')
for row in arr:
    print(row)

for row in arr:
    row[0], row[4] = row[4], row[0]

print('After swapping columns: ')
for row in arr:
    print(row)