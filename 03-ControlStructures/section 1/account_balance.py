account_balance = 500
total_payment = int(input("You are paying: "))

if total_payment < account_balance:
    print('Payment completed')
else:
    print('No funds')