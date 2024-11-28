def create_2d_arr(x,y):
    arr = [[0 for _ in range(y)] for _ in range(x)]
    return arr

for row in create_2d_arr(5, 9):
    print(row)
print()