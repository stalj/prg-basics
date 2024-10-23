n = int(10)
i = 0
sum_even = 0

while i < n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {n} is: {sum_even}")