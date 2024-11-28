def identity_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_matrix(m):
    for row in m:
        print(' '.join(map(str, row)))

x = identity_matrix(8)
print_matrix(x)