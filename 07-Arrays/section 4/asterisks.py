arr = [2, 6, 4, 9, 7]

def star(n):
    counter = 0
    while counter < n:
        print('*', end='')
        counter += 1
    print()

for num in arr:
    print(f'{num}: ', end='')
    star(num)