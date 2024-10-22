def negative_even(x,y):
    even_negatives=0
    for i in range(x, y+1):
        if i < 0 and i % 2 ==0:
            even_negatives+=1

    return even_negatives
