###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input('Temperature in C: '))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print('It is warm')
elif temperature >= 0:
    print('It is cold')
else:
    print('Warning, frost')