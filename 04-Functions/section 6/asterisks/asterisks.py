def f(num):
    list = []
    for i in range(num):
        list.append('*')
        if '/' not in list[-1:] and i != num - 1:
            list.append('/')
    for i in list:
        print(i, end='')