def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

any_number = int(input('Enter integer number: '))
any_number = abs(any_number)
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')