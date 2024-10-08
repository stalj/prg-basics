import random
dice = random.randint(1,6)
guess = int(input("Guess dice number: "))
guessed = dice == guess
print(f"You won: {guessed}, Correct number: {dice}")