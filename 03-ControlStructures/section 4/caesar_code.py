plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    new_char = ord(char) + 1
    encrypted_text += (chr(new_char))

print(plain_text)
print(encrypted_text)