def fibonacci (ranged):
    list = []
    for i in range(ranged + 1):
        if i == 0:
            list.append(i)
        elif i == 1:
            list.append(i)
        else:
            list.append(list[i - 1] + list[i - 2])
    for char in list:
        print(char, end=' ')

fibonacci(20)