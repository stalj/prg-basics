sum = 0

for i in range(10):
    if not i%2 == 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')