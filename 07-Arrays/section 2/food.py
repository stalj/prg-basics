categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_val = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[len(expenses) - 1]:
        max_val = categories[i]

print(max_val, ' is the most expensive category')