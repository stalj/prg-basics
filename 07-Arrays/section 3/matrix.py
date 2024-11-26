matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

i = 0
for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    for char in row:
        print(char, end=' ')
    print()