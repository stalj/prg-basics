arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr) - 1)
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[4])
print('Sum of first and last value', arr[0] + arr[-1])
print('Middle value', arr[int((len(arr)/2))])
for i in arr:
    print(i, end=' ')