def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

x = [5, 4, 6, 7, 8, 9, 0, 1]
print(bubble_sort(x))