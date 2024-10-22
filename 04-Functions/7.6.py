def even(liczba):
    if liczba%2==0:
        return True
    else:
        return False
x=int(input('Podaj liczbe: '))
print('Liczba jest parzysta:', even(x))