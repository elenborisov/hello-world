import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.set(xlabel='x', ylabel='sin(x)', title='SIN(X)')

plt.show()