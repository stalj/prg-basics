import math
def triangle_area(a,b,c):
    p=(a+b+c)/2
    surface=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return surface
surface=triangle_area(7,24,25)
print(surface)