def f (entry):
    n = 0
    check_list = []
    for i in range(len(entry)):
        if entry[i] == '+':
            n += 1
        if entry[i] == '-':
            n -= 1
        if n >= 3:
            check_list.append(True)
        else:
            check_list.append(False)
    if True in check_list:
        return True
    else:
        return False