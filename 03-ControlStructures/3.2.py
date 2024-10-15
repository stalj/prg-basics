###
# Checking login and password
#
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')