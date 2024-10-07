import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5*np.pi, 0.1)
y = np.cos(x)

plt.axhline(y = 0, color = 'k', linewidth = 1)     
plt.plot(x, y)
plt.show()

