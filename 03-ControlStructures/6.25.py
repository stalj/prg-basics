#The payment card is secured with a four-digit PIN code (0805). 
#Write a program that checks if the PIN code entered in the payment terminal is correct. 
#The user has up to three possibilities for entering a PIN code.
# In case of three unsuccessful attempts, the card is blocked. Sample result:
correct_pin = '0805'
block=0
for x in range(1,4):
    pin = input('Enter 4-digit PIN code: ')
    if pin==correct_pin:
        print('PIN is correct')
        break
    else:
        print('PIN is incorrect')
        block+=1
if block==3:
    print('Sorry, your payment card has been blocked.')