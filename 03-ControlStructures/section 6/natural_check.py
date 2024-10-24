# 1. A natural number greater than 1 is called a prime if it has exactly 
# 2 natural factors with the values 1 and this number. Write a program that 
# finds N leading prime numbers. Read the value of N from the keyboard. Using 
# loop statements check that the number N is divisible only by 1 and by N.

#     Prime numbers: 2 3 5 7 11 ...

is_prime = True

num = int(input('Enter a prime number: '))

if num < 2:
    is_prime = False
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False

if is_prime:
    print(f'Is a prime number: {is_prime}')
else:
    print(f"{num} is not a prime number")