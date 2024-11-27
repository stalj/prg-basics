even_numbers = []
odd_numbers = []

array = [4, 8, 1, 3, 6, 8, 4, 1, 1, 9, 7, 4, 5, 7, 3, 6]
for num in array:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(even_numbers + odd_numbers)