# IPython log file

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 4.5, 0.5)
y2 = x**2
y3 = x**3

plt.plot(x, x, 'r-', label= 'f(x)')
plt.plot(x, y2, 'b-', label= 'g(x)')
plt.plot(x, y3, 'g-', label= 'h(x)')
plt.plot(x, x, '.')
plt.plot(x, y2, '.')
plt.plot(x, y3, '.')
plt.title("Plotting in python")
plt.xlabel("x value")
plt.ylabel("y value")
plt.savefig("plotting.png")
