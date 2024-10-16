parked_time = int(input('Numbers of hours that you parked: '))
if parked_time>6:
    print('Fee: 20PLN')
elif parked_time>3:
    print('Fee: 15PLN')
elif parked_time>0:
    print('Fee: 5PLN')
else:
    print('Wrong hours')