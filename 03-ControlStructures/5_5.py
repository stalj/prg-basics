###
# Sums numbers entered by user
#
total_sum = 0
numbers_value = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    numbers_value +=1
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number

print(f"The arithmetic mean of the numbers is: {total_sum/numbers_value}")