# 1. Write a program that converts a decimal number into a binary number. To convert
# a decimal number to binary, follow these steps:

#     1. Read a decimal number from the keyboard.
#     1. Divide the number by 2 and note the remainder.
#     1. Divide the quotient obtained by 2 and note the remainder.
#     1. Repeat the same process till we get 0 as the quotient.
#     1. Write the values of all the remainders starting from the bottom to the top. 
# That will be the required binary number.

#     Sample result:

#     Enter decimal number: 12\
#     12(10) = 1100(2)

import math
num = int(input("Enter a decimal number: "))
saved_num = num
binary = ''

if num < 0:
    print('Negative numbers are not supported')

if num == 0:
    print('0')

while num > 0:
    remainder = num % 2
    binary += str(remainder)
    num //= 2

print(f"{saved_num}(10) in binary is {binary[::-1]}(2)")