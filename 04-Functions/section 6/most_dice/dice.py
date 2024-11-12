def check_max(number):
    res = [0] * 10
    for digit in str(number):
        res[int(digit)] += 1
    print(res.index(max(res)))