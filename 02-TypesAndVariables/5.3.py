###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
cuboid_volume=a*b*c
cuboid_surface=2*(a*b+a*c+b*c)
print(f"Cuboid of dimensions: {a}, {b}, {c} has a volume of {cuboid_volume}")
print(f"Cuboid of dimensions: {a}, {b}, {c} has a surface area of {cuboid_surface}")