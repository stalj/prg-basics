def sumowanie_cyfr(liczba, even):
    suma=0
    if even==True:
        for i in range(len(liczba)):
            if int(liczba[i]) % 2 == 0:
                suma+=int(liczba[i])
    else:
        for i in range(len(liczba)):
            if int(liczba[i]) % 2 != 0:
                suma+=int(liczba[i])
    return suma
