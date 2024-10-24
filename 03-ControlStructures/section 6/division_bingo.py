res = []
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        res.append('\BINGO/')
    elif i % 3 == 0:
        res.append('\Three/')
    elif i % 5 == 0:
        res.append('\Five/')
    else:
        res.append(str(i))

print(' '.join(res))