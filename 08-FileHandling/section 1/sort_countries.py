def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('countries.txt')

file_lines = file_content.splitlines()
file_lines.sort()

for line in file_lines:
   print(line)