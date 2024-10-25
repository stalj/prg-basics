def special_code(product_code):
    suma=0
    if len(product_code)==4 and product_code.isdigit()==True:
        for i in range (len(product_code)-1):
            suma+=int(product_code[i])
        ostatnia_cyfra=suma%7
        if ostatnia_cyfra==int(product_code[3]):
            return True
        else:
            return False
    else:
        return False