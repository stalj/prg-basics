###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end="")