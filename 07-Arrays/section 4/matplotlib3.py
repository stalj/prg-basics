import matplotlib.pyplot as plt
import math

x_degrees = range(0, 361)
y = [math.sin(math.radians(x)) for x in x_degrees]

plt.plot(x_degrees, y)
plt.show()