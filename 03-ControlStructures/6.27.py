x=0
y=1
z=1
k=2
for i in range(1,6):
    print(x, y, z, k, end=' ')
    x=k+z
    y=k+x
    z=x+y
    k=z+y


    
