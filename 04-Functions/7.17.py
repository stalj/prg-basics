#0,1,1,2,3,5,8,13,21
def get_nth_fibonacci(number):
    number1=0
    number2=1
    for i in range(number-1):
        number1, number2 = number2, number1+number2
    
    return number1    