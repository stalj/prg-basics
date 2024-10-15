account_balance = 500
total_payment = int(input("Total value of purchase: "))
if total_payment <= account_balance:
    print("Payment completed")
else:
    print("Insufficent funds")