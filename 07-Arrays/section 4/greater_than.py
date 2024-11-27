def count_greater_elements(value, arr):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

array = [3, 1, 4, 9, 2, 6]
print(count_greater_elements(2, array))