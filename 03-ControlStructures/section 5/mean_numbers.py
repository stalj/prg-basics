total_sum = 0
num_count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break 
    total_sum += number
    num_count += 1

print(f"The total sum of the numbers is: {total_sum}")
print(f"The total mean of the numbers is: {total_sum/(num_count - 1):.1f}")
