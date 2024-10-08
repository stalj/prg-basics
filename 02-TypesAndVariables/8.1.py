###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# display results

import math
radius = float(input("Radius: "))
area = math.pi*radius**2
circumference= 2*math.pi*radius
print(f"Area: {round(area, 2)}")
print(f"Circumference: {round(circumference, 2)}")