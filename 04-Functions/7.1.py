import mymath
import mykeyboard

number=mykeyboard.read_number()
right_number=mymath.generate_number()

if number==right_number:
    print('You won the game!!')