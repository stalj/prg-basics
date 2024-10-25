def sum_to_n(number):
    if number==1:
        return 1
    elif number>1:
        return number+sum_to_n(number-1)