def check_negative(n1, n2, n3):
    num_list = [True if n1 < 0 else False, True if n2 < 0 else False, True if n3 < 0 else False]
    if True in num_list:
        return True
    else:
        return False