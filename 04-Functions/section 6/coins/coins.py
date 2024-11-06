def amount_to_pay(num):
    num_of_fives = 0
    num_of_twos = 0
    num_of_ones = 0

    while num > 0:
        if num >= 5:
            num -= 5
            num_of_fives += 1
        elif num >= 2:
            num -= 2
            num_of_twos += 1
        elif num >= 1:
            num -= 1
            num_of_ones += 1
    
    return f'You need atleast {num_of_fives + num_of_ones + num_of_twos} coins'