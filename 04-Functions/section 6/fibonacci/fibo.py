def fibo(n):
    list = []
    for i in range(n):
        if i == 0:
            list.append(i)
        elif i == 1:
            list.append(i)
        else:
            list.append(list[i - 1] + list[i - 2])
    return list[n - 1]