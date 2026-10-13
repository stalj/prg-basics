###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    encrypted_text += chr(ord(char)+1)
    # add one to the character's code
    ...
    # replace new character code with its
    # corresponding character (use chr())
    ...
    # add encrypted character to encrypted text
    ...

print(plain_text)
print(encrypted_text)