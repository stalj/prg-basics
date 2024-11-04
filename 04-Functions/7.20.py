def sum_repeated(number):
    suma=0
    number_str=str(number)
    for i in range(10):
        count=number_str.count(str(i))
        if count>1:
            suma+=count*i    
    
    return suma