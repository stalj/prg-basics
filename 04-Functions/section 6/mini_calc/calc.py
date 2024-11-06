def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return f'{num1/num2:.2f}'
    elif op == '**':
        return num1**num2
    else:
        return 'Invalid data'