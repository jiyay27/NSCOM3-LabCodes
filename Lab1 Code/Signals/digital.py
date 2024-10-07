import matplotlib.pyplot as plt
import numpy as np

signal = [0.5,0,1,1,0,-0.5]

x = [0,1,2,3,4,5,6,7,8,9]
y = [0.5,0.5,0,1,1,0,0,-0.5,-0.5,0]
# x - periodic interval to show high and lows
# y - high and low values

plt.axhline(y = 0, color = 'k')

plt.step(x,y)
plt.show()


