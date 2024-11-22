def bubbleSort(arr):
   n = len(arr)
   for i in range(n - 1):
      for j in range(n-i-1):
         if arr[j] > arr[j+1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
   return arr
x = [5, 4, 6, 7, 8, 9, 0, 1]
print(bubbleSort(x))