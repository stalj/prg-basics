def check_e_n(min, max):
    n = 0

    while min < 0:
        if min % 2 == 0:
            n += 1
        min += 1
    return n