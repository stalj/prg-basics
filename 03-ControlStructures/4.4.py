###
# Displays the name of university where you are studying
# with an extra space between characters (add a space between
# each character)
#
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded += char + ' '

print(university)
print(university_expanded)