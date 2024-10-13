import random
computer = random.randint(1, 6)
is_running = True
while (is_running):
    you = int(input('Your guess: '))
    if you == computer:
        print(f'The number was {computer}. You win')
        is_running = False
    else:
        print('Try again')