

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 4.5, 0.5)
x2 = x**2
x3 = x**3

plt.plot(x, x, 'r-', label= 'f(x)=x')
plt.plot(x, x2, 'b-', label= 'g(x)=x2')
plt.plot(x, x3, 'g-', label= 'h(x)=x3')
plt.title("Plotting in python")
plt.xlabel("x value")
plt.ylabel("y value")
plt.legend()
plt.show()
plt.savefig("plotting.png")
