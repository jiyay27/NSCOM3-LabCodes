import math

def shannon_capacity(bandwidth, snr):
    capacity = bandwidth * math.log2(1 + snr)
    return capacity

bandwidth = 3000
snr = 3162
capacity = shannon_capacity(bandwidth, snr)
print(f"Shannon Capacity: {capacity:.2f} bps")






