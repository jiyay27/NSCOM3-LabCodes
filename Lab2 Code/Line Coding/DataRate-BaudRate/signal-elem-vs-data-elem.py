import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x, y, title, xlabel, ylabel):
    plt.axhline(0, color='black', linewidth=2)
    plt.step(x, y, where='mid', label='Signal', color='magenta', linewidth=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.ylim(-1.5, 1.5)
    plt.xlim(x[0] - 0.1, x[-1] + 0.1)

#figure a
plt.figure(figsize=(6, 4))
x_a = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y_a = np.array([1, -1, -1, 1, 1, -1, -1, 1])
plot_graph(x_a, y_a, "a. One data element per one signal element (r=1)", "Signal elements", "Data elements")
plt.show()

# figure b
plt.figure(figsize=(6, 4))
x_b = np.array([0, 1, 2, 3, 4, 5, 6])
y_b = np.array([1, -1, 1, -1, 1, -1, 1]) 
plot_graph(x_b, y_b, "b. One data element per two signal elements (r=1/2)", "Signal elements", "Data elements")
plt.show()

# figure c
plt.figure(figsize=(6, 4))
x_c = np.array([0, 1, 2, 3, 4, 5])
y_c = np.array([1, 1, -1, -1, 1, 1])
plot_graph(x_c, y_c, "c. Two data elements per one signal element (r=2)", "Signal elements", "Data elements")
plt.show()

# figure d
plt.figure(figsize=(6, 4))
x_d = np.array([0, 1, 2])
y_d = np.array([1, -1, 0])
plot_graph(x_d, y_d, "d. Four data elements per three signal elements (r=4/3)", "Signal elements", "Data elements")
plt.show()
