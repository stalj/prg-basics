array1 = [7, 3, 8, 5, 2]
array2 = [3, 7, 5]

expected = []
for value in array2:
    if value in array1:
        expected.append(value)

if expected == array2:
    print(f'{array2} is a subset of {array1}')
else:
    print(f'{array2} is not a subset of {array1}')