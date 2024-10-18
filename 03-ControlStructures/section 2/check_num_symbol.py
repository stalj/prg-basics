num = int(input('Enter a number: '))
if num == 0:
    print('Your number is not negative nor positive')
if num < 0:
    print(f'number: {num} is negative')
if num > 0:
    print(f'number: {num} is positive')