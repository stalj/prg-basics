arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

def convert_to_1d(a):
    li = []
    for row in a:
        li.extend(row)
    return li

print('Before: ')
for row in arr:
    print(row)

print('After: ')
print(convert_to_1d(arr))