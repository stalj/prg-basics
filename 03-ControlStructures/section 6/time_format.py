time = input("Enter time (24-hour format): ")

hours, minutes = map(int, time.split(':'))
if hours >= 12:
    period = 'PM'
else:
    period = 'AM'

if hours == 0:
    hours = 12
elif hours > 12:
    hours -= 12

print(f"{hours}:{minutes:02d} {period}")