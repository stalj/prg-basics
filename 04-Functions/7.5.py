def greater(liczba1, liczba2):
    if liczba1>liczba2:
        return True
    else:
        return False

x=int(input('Pierwsza liczba: '))
y=int(input('Druga liczba: '))
czy_wieksza=greater(x,y)
print(czy_wieksza)