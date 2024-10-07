import math

B = 1000  # sample value for B 
L = 10     # sample value for L

Nmax = 2 * B * math.log2(L)  # Formula for Nmax

print(f"Nmax: {Nmax:.8g}")
