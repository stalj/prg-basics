import keyboard1

first_name = keyboard1.input_string('Enter your first name: ')
last_name = keyboard1.input_string('Enter your last name: ')
age = keyboard1.input_integer('Enter your age: ')
salary = keyboard1.input_real('Enter your salary: ')
is_salary_hidden = keyboard1.input_boolean('Hide salary? (y/n)')

print()
print('DATA RECORD')
print('===========')
print('Name:', first_name, " ", last_name)
print('Age: ', age)

if is_salary_hidden == 'n':
    print('Salary: ', salary)
elif is_salary_hidden == 'y':
    print('Salary: hidden')
else:
    print('Invalid data')