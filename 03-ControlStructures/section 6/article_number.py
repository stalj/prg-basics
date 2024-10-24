ean13 = input('Enter EAN-13 article number: ')
if ean13.isdigit() == True and len(ean13) == 13:
    print('article number is correct')
    if ean13[0:3] == '590':
        print('article manufactured in Poland')
else:
    print('invalid article number')