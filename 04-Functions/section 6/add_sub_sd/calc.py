def add_sub(text):
    res = 0
    current_number = 0
    operation = '+'
    for i in text:
        if i.isdigit():
            current_number = int(i)
        else:
            if operation == '+':
                res += current_number
            elif operation == '-':
                res -= current_number
            operation = i
    if operation == '+':
        res += current_number
    elif operation == '-':
        res -= current_number
    return res
