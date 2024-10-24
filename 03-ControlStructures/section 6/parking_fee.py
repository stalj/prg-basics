hours = int(input("Enter the number of hours your car was parked for: "))
if hours == 1 or hours == 2:
    print("You must pay 5PLN")
elif hours == 3 or hours <= 6:
    print("You must pay 15PLN")
elif hours > 6:
    print("You must pay 20PLN")