###
# Reads a non-existent file
# with try-except block
#

# there is no file with this name on the disk
file_name = 'xyz.txt'

try:
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
    print(f"Hey! The file {file_name} does not exist.")