def occurs(number, array):
    if number in array:
        return f'number {number} appears in the array'
    else:
        return f'number {number} was not found'

number = 23
array = [15, 38, 7, 23, 14]
print('Number: ', number)
print('Array: ', ' '.join(map(str, array)))
print(occurs(number, array))