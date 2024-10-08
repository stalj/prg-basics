###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter secound letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
if(first==last): number_of_letters = 0
else: number_of_letters = last_letter_code-1-first_letter_code
print(f'Between {first} and {last} is {number_of_letters} letters')