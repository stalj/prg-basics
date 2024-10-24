index = 0
dog_age = 0
age = int(input("Enter your dogs age in dog years: "))

while index < age:
    index = index + 1
    if index == 1:
        dog_age += 10.5
    elif index == 2:
        dog_age += 10.5
    elif index > 2:
        dog_age += 4
print(dog_age)