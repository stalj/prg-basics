arr = [2, 3, 2, 5, 8, 1, 9, 8]

element_count = {}
for num in arr:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

unique_elements = [num for num, count in element_count.items() if count == 1]

print("Array: ", ' '.join(map(str, arr)))
print("Unique values: ", ' '.join(map(str, unique_elements)))