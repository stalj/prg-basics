###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter secound number: '))

if not x < 0 or y > 0:
    print(f'At least one of the numbers {x} and {y} is not negative')