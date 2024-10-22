import myrange
liczba=int(input('Liczba: '))
x=int(input('Przedział od: '))
y=int(input('Przedział do: '))
in_range=myrange.range(liczba, x, y)
if in_range==True:
    print(f'Liczba {liczba} mieści się w przedziale <{x},{y}>')
else:
    print(f'Liczba {liczba} nie mieści się w przedziale <{x},{y}>')