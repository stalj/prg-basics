def check_max(number):
    string = str(number)
    list_num = list(string)
    res = [0] * 10
    for i in list_num:
        res[int(i)] += 1
    print(res.index(max(res)))