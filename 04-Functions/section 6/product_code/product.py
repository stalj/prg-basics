def check_product(num):
    num_str = str(num)
    sum = 0
    if len(num_str) != 4:
        print('invalid length')
    else:
        for n in range(len(num_str)-1):
            digit = int(num_str[n])
            sum += digit
        if int(num_str[3]) == sum % 7:
            print('True')
            return num_str
        else:
            print('False')
            return num_str