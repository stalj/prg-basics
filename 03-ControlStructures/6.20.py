amount=int(input('Enter the amount in PLN: '))
coins5=0
coins2=0
coins1=0
while amount>=5:
    coins5+=1
    amount-=5
while amount>=2:
    coins2+=1
    amount-=2
while amount>=1:
    coins1+=1
    amount-=1
print(f'5 PLN coins: {coins5}')
print(f'2 PLN coins: {coins2}')
print(f'1 PLN coins: {coins1}')