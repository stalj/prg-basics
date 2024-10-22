###
# Calculates the sum of the digits in a number
#
def digit_sum(number):
    wynik=0
    string=str(number)
    for i in range (0, len(string)):
        wynik+=int(string[i])
    return wynik

any_number = int(input('Enter integer number: '))
result = digit_sum(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')