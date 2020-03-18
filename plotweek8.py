#exemplo week8 plotter

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 5.0, 1)

y1 = x
y2 = x**2
y3 = x**3

plt.plot(x, y1, 'g.', label="X**1")
plt.plot(x, y2, 'r.', label="X**2")
plt.plot(x, y3, 'b.', label="X**3")


plt.legend()
plt.title("WorkHome Week 8")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")

plt.ioff()
plt.show()
