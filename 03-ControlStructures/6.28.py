maksymalna_liczba=int(input('Maks number: '))
liczby_pierwsze=2
print('Prime numbers: ', end='')
while maksymalna_liczba>=liczby_pierwsze:
    not_prime=0
    for i in range(2, liczby_pierwsze):
        if liczby_pierwsze%i==0:
            not_prime+=1
    if not_prime==0:
        print(liczby_pierwsze, end=' ')
    liczby_pierwsze+=1