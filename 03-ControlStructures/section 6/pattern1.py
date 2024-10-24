res = []
for i in range (1, 11):
    if i < 6:
        res.append('\*/')
        for char in res:
            print(char, end=' ')
        print()
    elif i > 6:
        res.pop()
        for char in res:
            print(char, end=' ')
        print()