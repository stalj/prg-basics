#Write a program that creates the following pattern. Sample result:

#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999
x='1'
int_x=int(x)
while int_x<=9:
    print(x*int_x)
    int_x+=1
    x=str(int_x)

