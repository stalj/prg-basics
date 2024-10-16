decimal_num=int(input('Enter decimal number: '))
decimal_num0=decimal_num
binary_num=''
while decimal_num>0:
    if decimal_num%2==1:
        decimal_num-=1
        binary_num ='1'+binary_num
    else:
        binary_num='0'+binary_num
    decimal_num/=2
print(f'{decimal_num0}(10) = {(binary_num)}(2)')