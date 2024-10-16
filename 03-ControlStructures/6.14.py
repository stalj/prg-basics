EAN=input('Enter EAN-13 article number: ')
if len(EAN)==13:
    print('Article number is correct')
    if EAN[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')