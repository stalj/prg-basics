total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20
else:
    print('invalid choice')

if extra_rinse == 'y' and extra_spin == 'y':
    total_washing_time += 24
elif extra_rinse == 'y':
    total_washing_time += 15
elif extra_spin == 'y':
    total_washing_time += 9
else:
    total_washing_time += 0

extra_rinse = True if extra_rinse == 'y' else False
extra_spin = True if extra_spin == 'y' else False

print(f"washing product: {program}")
print(f"rinse: {extra_rinse}")
print(f"spin: {extra_spin}")
print(f"total washing time: {total_washing_time}")