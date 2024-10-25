# Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time 
# in the given format ('24' for 24-hour time and '12' for 12-hour time).

# Then write a program that tests whether the function works correctly.

# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 02, '12') returns '7:02pm'
# Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings'.

def time_string(hour, minute, format):
    if format == '24':
        if len(str(hour)) < 2 and len(str(minute)) < 2:
            print(f'0{hour}:0{minute}')
        elif len(str(hour)) < 2:
            print(f'0{hour}:{minute}')
        elif len(str(minute)) < 2:
            print(f'{hour}:0{minute}')
        else:
            print(f'{hour}:{minute}')
    elif format == '12':
        if hour > 12 and len(str(minute)) < 2:
            print(f'{hour - 12}:0{minute}')
        elif hour == 0 and len(str(minute)) < 2:
            print(f'{hour + 12}:0{minute}')
        elif hour > 12:
            print(f'{hour - 12}:{minute}')
        elif hour == 0:
            print(f'{hour + 12}:{minute}')
        else:
            print(f'{hour}:{minute}')

def main():
    time_string(15, 38, '24') 
    time_string(8, 3, '24') 
    time_string(0, 5, '24') 
    time_string(11, 15, '12') 
    time_string(0, 7, '12')
    time_string(7, 30, '12')
    time_string(12, 46, '12')
    time_string(13, 10, '12') 
    time_string(19, '02', '12') 

if __name__ == '__main__':
    main()