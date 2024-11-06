def sum_range(a, b):
    res = 0
    for i in range(a, b + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0: 
            res += i
    return res