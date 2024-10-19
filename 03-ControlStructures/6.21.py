x=0
while x<30:
    x+=1
    if x%3!=0 and x%5!=0:
        print(x)
    elif x%3==0 and x%5==0:
        print('BINGO')
    elif x%3==0:
        print('THREE')
    elif x%5==0:
        print('FIVE')