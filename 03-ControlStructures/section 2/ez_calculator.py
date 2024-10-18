number1 = input('Enter the first number: ')
operator = input('Choose an operation: ')
number2 = input('Enter the second number: ')
result = 0
if operator == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operator == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operator == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operator == '/':
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")
else:
    print('invalid')