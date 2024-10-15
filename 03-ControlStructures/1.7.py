###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = bool(int(input("Bonus included(1-yes, 0-no): ")))

if is_bonus:
    bonus = float(input("Bonus (%): "))
    total_salary = basic_salary + basic_salary*bonus*0.01
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')