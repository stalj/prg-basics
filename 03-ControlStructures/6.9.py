dog_age_in_human=int(input("Enter the dog's age in human years: "))
dog_age=0
if dog_age_in_human>=1:
    dog_age+=10.5
    if dog_age_in_human>=2:
        dog_age+=10.5

if dog_age_in_human>2:
    while dog_age_in_human > 2:
        dog_age+=4
        dog_age_in_human-=1
print(f"The dog's age in dog's years is {dog_age} years")