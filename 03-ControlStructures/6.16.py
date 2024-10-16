hours24=input('Enter time (24-hour format): ')
x = len(hours24)
int_hours=int(hours24[0:x-3])
if int_hours<24:
    if int_hours<12:
        hours24+='am'
    else:
       int_hours-=12
       hours24=str(int_hours)+hours24[x-3:x]
       hours24+='pm'
    print(f'Time in 12-hour format: {hours24}')