def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_mid(arr):
    bubble_sort(arr)
    if len(arr) % 2 == 1:
        x = len(arr) // 2
    else:
        x = arr[len(arr) // 2 - 1] + arr[len(arr) // 2]
        x = int(x / 2) + 1
    return x

def maxx(arr):
    initial = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - 1 > initial:
            initial = arr[i]
    return initial

def minn(arr):
    initial = arr[0]
    for i in range(len(arr)):
        if arr[i] < initial:
            initial = arr[i]
    return initial

def min_max(arr):
    n = []
    n.append(minn(arr))
    n.append(maxx(arr))
    return n

def second_max(arr):
    arr.remove(maxx(arr))
    return maxx(arr)

def diff(arr):
    return maxx(arr) - minn(arr)

def dashes(arr):
    return '-'.join(map(str, arr))

def display(arr):
    return ' '.join(map(str, arr))