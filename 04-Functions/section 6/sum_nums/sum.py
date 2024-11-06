def sum(n):
    sum_num = 0
    if n < 0:
        print('invalid')
    else:
        for i in range(1, n + 1):
            sum_num += i
    return sum_num