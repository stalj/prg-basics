balance = 1000 
pin = '1111' 

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check pin")
    print("5. Change pin")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        if pin.isdigit() == True and len(pin) == 4:
            print(f"Your pin is: {pin}")
        else:
            print(f"Please enter a valid pin code")
    elif choice == '5':
        pin = input("Enter the new pin code: ")
        if pin.isdigit() == True and len(pin) == 4:
            print(f"Your pin was changed to: {pin}")
        else: 
            print("Please enter a valid pin code")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break 
    else:
        print("Invalid option. Please try again.")
