age=int(input('Your age: '))
if age>=65:
    print('You are a Senior')
elif age>=20 and age<65:
    print('You are an Adult')
elif age>=13 and age<=19:
    print('You are a Teen')
elif age<13 and age>=0:
    print('You are a Child')
else:
    print('You werent born yet')