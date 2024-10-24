num = int(input('Enter the amount in PLN: '))
saved_num = num
num_of_fives = 0
num_of_twos = 0
num_of_ones = 0

while num > 0:
    if num >= 5:
        num -= 5
        num_of_fives += 1
    elif num >= 2:
        num -= 2
        num_of_twos += 1
    elif num >= 1:
        num -= 1
        num_of_ones += 1
        

print(f"{saved_num}PLN is: ")
print(f"5 PLN coins: {num_of_fives}")
print(f"2 PLN coins: {num_of_twos}")
print(f"1 PLN coins: {num_of_ones}")