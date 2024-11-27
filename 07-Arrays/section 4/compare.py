arr1 = ["water", "book", "sky"]
arr2 = ["water", "book", "sky"]

arr3 = [True, False]
arr4 = [True, False, True]

arr5 = [5, 3, 1]
arr6 = [5, 3, 1]

arr7 = [3, 2, 1]
arr8 = [3, 2]

def compare(array1, array2):
    if array1 == array2:
        return f'Comparison: arrays are the same'
    else:
        return f'Comparison: arrays are not the same'

def printf(arr):
    for char in arr:
        print(char, end=' ')
    print()

printf(arr1)
printf(arr2)
print()
        
print(compare(arr1, arr2))
print()

printf(arr3)
printf(arr4)
print()

print(compare(arr3, arr4))
print()

printf(arr5)
printf(arr6)
print()

print(compare(arr5, arr6))
print()

printf(arr7)
printf(arr8)
print()

print(compare(arr7, arr8))
print()