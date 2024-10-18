speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')