car_speed = int(input('Enter your car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < 0:
    print('Stop moving backwards!')
elif speed_limit_min < car_speed and car_speed < speed_limit_max:
    print('Your speed is okay!')
elif speed_limit_min < car_speed and car_speed > speed_limit_max:
    print('You are speeding! Slow down!')
elif speed_limit_min > car_speed:
    print('You are too slow!')
else: 
    print('invalid data')