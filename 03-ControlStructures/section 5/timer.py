import time

timer = int(input("Enter the countdown time in seconds: "))
while timer > 0:
    if timer > 5:
        print(timer)
    time.sleep(1)
    timer -= 1
    if timer == 5:
        print('five')
    elif timer == 4:
        print('four')
    elif timer == 3:
        print('three')
    elif timer == 2:
        print('two')
    elif timer == 1:
        print('one')

