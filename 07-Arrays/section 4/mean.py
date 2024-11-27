arr = [15, 8, 31, 47, 2, 19]

for char in arr:
    print(char, end=' ')
print()

#For loop
totalfor = 0
for value in arr:
    totalfor += value

meanfor = totalfor / len(arr)
print(int(meanfor))

#While loop
totalwhile = 0
counter = 0
while counter < len(arr):
    totalwhile += arr[counter]
    counter += 1

meanwhile = totalwhile / len(arr)
print(int(meanwhile))