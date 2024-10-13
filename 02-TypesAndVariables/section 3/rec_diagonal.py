import math

def calc_rec_diagonal (side1, side2) :
    diagonal = math.sqrt((side2**2) + (side1**2))
    print(f"The of {side1}cm and {side2}cm rectangle diagonal is {diagonal}cm")

calc_rec_diagonal(8, 5)