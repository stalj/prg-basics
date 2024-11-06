def calc(num, even):
    digit_str = str(num)
    total_sum = 0

    for digit in digit_str:
        digit_num = int(digit)
        if even:
            if digit_num % 2 == 0:
                total_sum += digit_num
        else:
            if digit_num % 2 != 0:
                total_sum += digit_num
            
    return total_sum