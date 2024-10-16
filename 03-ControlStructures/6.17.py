x = int(input('x = '))
y = int(input('y = '))
if x!=0 and y!=0:
    if x*y>0:
        if x>0:
            quadrant='the first'
        else:
            quadrant='third'
    else:
        if x>0:
            quadrant='fourth'
        else:
            quadrant='secound'
    print(f'Point P({x},{y}) is in {quadrant} quadrant of the coordinate system')
else:
    if x==0 and y==0:
        print('Point P(0,0) is located in the position (0,0) of the coordinate system')
    elif x!=0:
        print(f'Point P({x},{y}) is located on horizontal axis')
    else:
        print(f'Point P({x},{y}) is located on vertical axis')