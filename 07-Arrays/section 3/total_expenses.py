# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  
   [180, 60, 110],  
   [220, 55, 105], 
   [210, 65, 95]   
]

each_food = 0
each_transport = 0
each_utility = 0
for row in monthly_expenses:
    each_food += row[0]
    each_transport += row[1]
    each_utility += row[2]

def calc_week(n):
    n -= 1
    week = 0
    for row in monthly_expenses[n]:
        week += row
    return week

week1 = calc_week(1)
week2 = calc_week(2)
week3 = calc_week(3)
week4 = calc_week(4)

total = week1 + week2 + week3 + week4


print('MONTHLY EXPENSES')
print('----------------')
print('Food:', each_food)
print('Transport:', each_transport)
print('Utilities:', each_utility)
print('Week 1:', week1)
print('Week 2:', week2)
print('Week 3:', week3)
print('Week 4:', week4)
print('---------------')
print('TOTAL:', total)