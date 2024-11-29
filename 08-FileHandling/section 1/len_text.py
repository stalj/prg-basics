def read_file(file):
    with open(f"{file}.txt",  "r") as file:
        content = file.read()
    return content

rc = read_file('pan_kotek')
splited_rc = rc.split()

for i in range(len(splited_rc)):
    words = i

print(words)