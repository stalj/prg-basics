arr = [
    [-38, 19], 
    [5, 40],
    [-7, 11],
    [29, 16]
]

minimum = arr[0][0]
maximum = arr[0][0]

min_pos = (-1, -1)
max_pos = (-1, -1)
for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value < minimum:
            minimum = value
            min_pos = (i, j)
        if value > maximum:
            maximum = value
            max_pos = (i, j)

print(f'Smallest value {minimum} is at row {min_pos[0]} and column {min_pos[1]}')
print(f'Largest value {maximum} is at row {max_pos[0]} and column {max_pos[1]}')