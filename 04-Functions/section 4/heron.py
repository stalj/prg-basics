import math
def triangle_area(a,b,c):
    p = (a+b+c)/2
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return result

side1 = 12
side2 = 11
side3 = 6

print(f'The area of ​​a triangle with sides {side1} {side2} {side3} is {triangle_area(side1, side2, side3)}')