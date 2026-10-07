###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if i%2!=0:
        continue
    else:
        sum+=i

print(f'Sum of even numbers in the range <1,10> is {sum}')