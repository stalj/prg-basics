###
# A program that displays results of three dice rolls
# and the sum of dice rolled.
#
import random
first_dice = random.randint(1,6)
secound_dice = random.randint(1,6)
third_dice = random.randint(1,6)
print(f"First dice: {first_dice}")
print(f"Secound dice: {secound_dice}")
print(f"Third dice: {third_dice}")
print(f"Sum of three dice rolls: {first_dice+secound_dice+third_dice}")