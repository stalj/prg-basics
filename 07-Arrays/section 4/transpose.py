def transpose_matrix(m):
    row = len(m)
    col = len(m[0])

    transposed = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            transposed[j][i] = m[i][j]
    return transposed

def print_matrix(m):
    for row in m:
        print(' '.join(map(str, row)))

mx = [
    [-7,  12, 38],
    [41, -19, 11]
]

print('Before: ') 
print_matrix(mx)
x = transpose_matrix(mx)
print('After: ')
print_matrix(x)