def calculator(number1, number2, operator):
    if operator=="+":
        return number1+number2
    if operator=='-':
        return number1-number2
    if operator=='*':
        return number1*number2
    if operator=='%':
        return number1%number2
    if operator == '**':
        return number1**number2
print(calculator(2,3,'+'))