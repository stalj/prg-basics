###
# Sums numbers entered by user
#
total_sum = 0
i=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    i += 1

mean = total_sum/i
print(f"The total sum of the numbers is: {total_sum}")
print(f"The mean of the numbers is: {mean}")