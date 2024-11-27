names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

initial_name = ''
for name in names:
    if len(name) > len(initial_name):
        initial_name = name

print(initial_name)