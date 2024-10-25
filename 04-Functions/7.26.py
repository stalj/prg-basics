def suma_podzielnych_przez_6_nie4(x,y):
    suma=0
    for i in range(x,y+1):
        if i%6==0 and i%4!=0:
            suma+=i
    
    return suma