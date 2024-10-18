x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 and not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
elif x < 0 or y < 0:
    print(f'At least one of the numbers {x} and {y} is negative')
else:
    print('invalid result')