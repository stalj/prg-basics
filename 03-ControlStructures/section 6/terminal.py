correct_pin = '0805'
attempts = 0
while attempts != 3:
    pin = input('Enter the PIN code: ')
    if pin != correct_pin:
        print('INCORRECT')
    else:
        print("You have entered the correct PIN code")
        break
    attempts += 1
    if attempts == 3:
        print("Sorry, your payment card has been blocked")